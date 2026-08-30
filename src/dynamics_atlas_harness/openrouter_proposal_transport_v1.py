"""Thin, tool-less OpenRouter transport for typed proposal calls.

The repository remains the workflow orchestrator.  This module sends exactly one
strict JSON-Schema request for one explicit role/case/model/provider cell, records
transport provenance, and never authorizes or executes a scientific action.  It
contains no model router, retry loop, tool interface, or scientific decision logic.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
import time
import urllib.error
import urllib.request
import uuid
from collections.abc import Callable, Mapping
from contextlib import contextmanager
from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator


OPENROUTER_CHAT_COMPLETIONS_URL = "https://openrouter.ai/api/v1/chat/completions"
OPENROUTER_PROPOSAL_RECEIPT_SCHEMA = "openrouter-proposal-call-receipt/v1"
OPENROUTER_BUDGET_LEDGER_SCHEMA = "openrouter-budget-ledger/v1"
_CANONICALIZATION = "SORTED_KEYS_COMPACT_JSON_UTF8_V1"
_SECRET_TOKEN_PATTERN = re.compile(r"(?i)(?:sk-or-v1-|sk-)[A-Za-z0-9_-]{8,}")
_AUTHORIZATION_PATTERN = re.compile(r"(?i)authorization\s*[:=]\s*bearer\s+\S+")


class OpenRouterProposalTransportError(ValueError):
    """Raised before transport when a fail-closed call contract is invalid."""


def _canonical_json(value: Any) -> str:
    try:
        return json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
    except (TypeError, ValueError) as error:
        raise OpenRouterProposalTransportError("JSON_SERIALIZABLE_VALUE_REQUIRED") from error


def canonical_json_sha256(value: Any) -> str:
    return hashlib.sha256(_canonical_json(value).encode("utf-8")).hexdigest()


def text_sha256(value: str) -> str:
    if not isinstance(value, str):
        raise OpenRouterProposalTransportError("TEXT_VALUE_REQUIRED")
    return hashlib.sha256(value.encode("utf-8")).hexdigest()


def _nonempty_string(value: Any, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise OpenRouterProposalTransportError(f"NONEMPTY_STRING_REQUIRED:{label}")
    return value.strip()


def _nonnegative_decimal(value: Any, label: str) -> Decimal:
    try:
        result = value if isinstance(value, Decimal) else Decimal(str(value))
    except (InvalidOperation, ValueError) as error:
        raise OpenRouterProposalTransportError(f"FINITE_NONNEGATIVE_DECIMAL_REQUIRED:{label}") from error
    if not result.is_finite() or result < 0:
        raise OpenRouterProposalTransportError(f"FINITE_NONNEGATIVE_DECIMAL_REQUIRED:{label}")
    return result


def _positive_integer(value: Any, label: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
        raise OpenRouterProposalTransportError(f"POSITIVE_INTEGER_REQUIRED:{label}")
    return value


@dataclass(frozen=True, repr=False)
class OpenRouterCredential:
    """In-memory credential whose string representation never reveals its secret."""

    _secret: str = field(repr=False)
    source: str

    def __post_init__(self) -> None:
        object.__setattr__(
            self, "_secret", _nonempty_string(self._secret, "OPENROUTER_API_KEY")
        )
        if self.source not in {
            "INHERITED_ENVIRONMENT",
            "REPOSITORY_ENV_LOCAL",
            "REPOSITORY_ENV",
        }:
            raise OpenRouterProposalTransportError("CREDENTIAL_SOURCE_INVALID")

    def authorization_header(self) -> str:
        """Reveal the credential only at the HTTP-header construction boundary."""

        return f"Bearer {self._secret}"

    def contains(self, text: str) -> bool:
        return bool(self._secret and self._secret in text)

    def __repr__(self) -> str:
        return f"OpenRouterCredential(source={self.source!r}, secret=<redacted>)"

    __str__ = __repr__


def _dotenv_value(path: Path) -> str | None:
    """Read only OPENROUTER_API_KEY from one already-approved repository file."""

    observed: list[str] = []
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except (OSError, UnicodeDecodeError) as error:
        raise OpenRouterProposalTransportError("REPOSITORY_CREDENTIAL_FILE_UNREADABLE") from error
    for raw_line in lines:
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("export "):
            line = line[7:].lstrip()
        if "=" not in line:
            continue
        name, raw_value = line.split("=", 1)
        if name.strip() != "OPENROUTER_API_KEY":
            continue
        value = raw_value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
            value = value[1:-1]
        observed.append(value)
    if len(observed) > 1:
        raise OpenRouterProposalTransportError("DUPLICATE_OPENROUTER_API_KEY")
    if not observed:
        return None
    return _nonempty_string(observed[0], "OPENROUTER_API_KEY")


def read_openrouter_credential(
    *,
    repo_root: str | Path,
    environment: Mapping[str, str] | None = None,
) -> OpenRouterCredential:
    """Read only the inherited environment or exact repository-root env files.

    Resolution order is inherited ``OPENROUTER_API_KEY``, ``.env.local``, then
    ``.env``.  The function never scans parent directories, the home directory,
    shell history, keychains, or unrelated files.
    """

    environment = os.environ if environment is None else environment
    inherited = environment.get("OPENROUTER_API_KEY")
    if isinstance(inherited, str) and inherited.strip():
        return OpenRouterCredential(inherited.strip(), "INHERITED_ENVIRONMENT")

    root = Path(repo_root).resolve()
    if not root.is_dir():
        raise OpenRouterProposalTransportError("REPOSITORY_ROOT_REQUIRED")
    for filename, source in (
        (".env.local", "REPOSITORY_ENV_LOCAL"),
        (".env", "REPOSITORY_ENV"),
    ):
        candidate = (root / filename).resolve()
        if candidate.parent != root:
            raise OpenRouterProposalTransportError("REPOSITORY_CREDENTIAL_PATH_INVALID")
        if not candidate.is_file():
            continue
        value = _dotenv_value(candidate)
        if value is not None:
            return OpenRouterCredential(value, source)
    raise OpenRouterProposalTransportError("LIVE_CALL_BLOCKED_MISSING_CREDENTIAL")


@dataclass(frozen=True)
class OpenRouterModelSpec:
    """One exact catalog-approved model/provider and its frozen request settings."""

    model_id: str
    provider_endpoint_tag: str
    expected_provider_display_name: str
    prompt_price_per_token_usd: Decimal
    completion_price_per_token_usd: Decimal
    request_price_usd: Decimal = Decimal("0")
    metadata_sha256: str | None = None
    accepted_returned_model_ids: tuple[str, ...] = ()
    allowed_service_tiers: tuple[str | None, ...] = (None, "default")
    include_temperature_zero: bool = False
    reasoning_effort: str | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "model_id", _nonempty_string(self.model_id, "model_id"))
        object.__setattr__(
            self,
            "provider_endpoint_tag",
            _nonempty_string(self.provider_endpoint_tag, "provider_endpoint_tag"),
        )
        object.__setattr__(
            self,
            "expected_provider_display_name",
            _nonempty_string(
                self.expected_provider_display_name,
                "expected_provider_display_name",
            ),
        )
        object.__setattr__(
            self,
            "prompt_price_per_token_usd",
            _nonnegative_decimal(
                self.prompt_price_per_token_usd, "prompt_price_per_token_usd"
            ),
        )
        object.__setattr__(
            self,
            "completion_price_per_token_usd",
            _nonnegative_decimal(
                self.completion_price_per_token_usd,
                "completion_price_per_token_usd",
            ),
        )
        object.__setattr__(
            self,
            "request_price_usd",
            _nonnegative_decimal(self.request_price_usd, "request_price_usd"),
        )
        if self.metadata_sha256 is not None and not re.fullmatch(
            r"[0-9a-f]{64}", self.metadata_sha256
        ):
            raise OpenRouterProposalTransportError("MODEL_METADATA_SHA256_INVALID")
        if not isinstance(self.accepted_returned_model_ids, tuple):
            raise OpenRouterProposalTransportError(
                "ACCEPTED_RETURNED_MODEL_IDS_TUPLE_REQUIRED"
            )
        accepted_ids = tuple(
            dict.fromkeys(
                _nonempty_string(value, "accepted_returned_model_ids")
                for value in self.accepted_returned_model_ids
            )
        )
        if self.model_id not in accepted_ids:
            accepted_ids = (self.model_id, *accepted_ids)
        object.__setattr__(self, "accepted_returned_model_ids", accepted_ids)
        if (
            not isinstance(self.allowed_service_tiers, tuple)
            or not self.allowed_service_tiers
            or any(
                value is not None and (not isinstance(value, str) or not value)
                for value in self.allowed_service_tiers
            )
        ):
            raise OpenRouterProposalTransportError(
                "ALLOWED_SERVICE_TIERS_TUPLE_REQUIRED"
            )
        if not isinstance(self.include_temperature_zero, bool):
            raise OpenRouterProposalTransportError(
                "INCLUDE_TEMPERATURE_ZERO_BOOLEAN_REQUIRED"
            )
        if self.reasoning_effort is not None:
            normalized_effort = _nonempty_string(
                self.reasoning_effort, "reasoning_effort"
            ).lower()
            if normalized_effort not in {
                "none",
                "minimal",
                "low",
                "medium",
                "high",
                "xhigh",
            }:
                raise OpenRouterProposalTransportError("REASONING_EFFORT_INVALID")
            object.__setattr__(self, "reasoning_effort", normalized_effort)


@dataclass(frozen=True)
class BudgetReservation:
    role: str
    case_id: str
    model_id: str
    attempt_number: int
    worst_case_cost_usd: Decimal
    reservation_id: str
    campaign_id: str | None = None

    @property
    def cell_key(self) -> tuple[str, str, str]:
        return (self.role, self.case_id, self.model_id)


class OpenRouterBudgetLedger:
    """Fail-closed budget and call-count ledger for one campaign.

    The default remains an in-memory ledger for programmatic tests.  Supplying a
    campaign ID and state path enables a cross-process ledger.  Every reservation
    is written before transport, and any unresolved reservation or unknown cost
    blocks later calls rather than silently resetting campaign authority.
    """

    def __init__(
        self,
        *,
        cap_usd: Decimal | str | float,
        max_completed_calls: int = 16,
        max_attempts_per_cell: int = 2,
        campaign_id: str | None = None,
        state_path: str | Path | None = None,
    ) -> None:
        self.cap_usd = _nonnegative_decimal(cap_usd, "cap_usd")
        if self.cap_usd == 0:
            raise OpenRouterProposalTransportError("POSITIVE_CAMPAIGN_CAP_REQUIRED")
        self.max_completed_calls = _positive_integer(
            max_completed_calls, "max_completed_calls"
        )
        self.max_attempts_per_cell = _positive_integer(
            max_attempts_per_cell, "max_attempts_per_cell"
        )
        self.actual_cost_usd = Decimal("0")
        self.completed_calls = 0
        self.attempts_by_cell: dict[tuple[str, str, str], int] = {}
        self.reported_cost_available = True
        self.campaign_id = (
            _nonempty_string(campaign_id, "campaign_id")
            if campaign_id is not None
            else None
        )
        self._state_path = Path(state_path).resolve() if state_path is not None else None
        self._inflight_reservation: BudgetReservation | None = None
        if (self.campaign_id is None) is not (self._state_path is None):
            raise OpenRouterProposalTransportError(
                "PERSISTED_BUDGET_REQUIRES_CAMPAIGN_ID_AND_STATE_PATH"
            )
        if self._state_path is not None:
            self._initialize_persisted_state()

    @property
    def persisted(self) -> bool:
        return self._state_path is not None

    @property
    def state_path(self) -> Path | None:
        """Expose the local path to the caller, never to persisted receipts."""

        return self._state_path

    @property
    def _lock_path(self) -> Path:
        if self._state_path is None:
            raise OpenRouterProposalTransportError("PERSISTED_BUDGET_STATE_REQUIRED")
        return self._state_path.with_name(self._state_path.name + ".lock")

    @contextmanager
    def _exclusive_lock(self):
        if self._state_path is None:
            yield
            return
        self._state_path.parent.mkdir(parents=True, exist_ok=True)
        try:
            descriptor = os.open(
                self._lock_path,
                os.O_CREAT | os.O_EXCL | os.O_WRONLY,
                0o600,
            )
        except FileExistsError as error:
            raise OpenRouterProposalTransportError(
                "BUDGET_LEDGER_LOCKED_OR_PREVIOUS_PROCESS_UNRESOLVED"
            ) from error
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                handle.write(f"{self.campaign_id}\n")
                handle.flush()
                os.fsync(handle.fileno())
            yield
        finally:
            try:
                self._lock_path.unlink()
            except FileNotFoundError:
                pass

    def _initial_state(self) -> dict[str, Any]:
        return {
            "schema_version": OPENROUTER_BUDGET_LEDGER_SCHEMA,
            "campaign_id": self.campaign_id,
            "cap_usd": str(self.cap_usd),
            "max_completed_calls": self.max_completed_calls,
            "max_attempts_per_cell": self.max_attempts_per_cell,
            "actual_cost_usd": "0",
            "completed_calls": 0,
            "attempts_by_cell": [],
            "reported_cost_available": True,
            "inflight_reservation": None,
        }

    def _state_from_memory(self) -> dict[str, Any]:
        inflight = self._inflight_reservation
        return {
            "schema_version": OPENROUTER_BUDGET_LEDGER_SCHEMA,
            "campaign_id": self.campaign_id,
            "cap_usd": str(self.cap_usd),
            "max_completed_calls": self.max_completed_calls,
            "max_attempts_per_cell": self.max_attempts_per_cell,
            "actual_cost_usd": str(self.actual_cost_usd),
            "completed_calls": self.completed_calls,
            "attempts_by_cell": [
                {
                    "role": role,
                    "case_id": case_id,
                    "model_id": model_id,
                    "attempts": attempts,
                }
                for (role, case_id, model_id), attempts in sorted(
                    self.attempts_by_cell.items()
                )
            ],
            "reported_cost_available": self.reported_cost_available,
            "inflight_reservation": (
                None
                if inflight is None
                else {
                    "role": inflight.role,
                    "case_id": inflight.case_id,
                    "model_id": inflight.model_id,
                    "attempt_number": inflight.attempt_number,
                    "worst_case_cost_usd": str(inflight.worst_case_cost_usd),
                    "reservation_id": inflight.reservation_id,
                }
            ),
        }

    def _validate_and_load_state(self, raw_state: Any) -> None:
        if not isinstance(raw_state, Mapping):
            raise OpenRouterProposalTransportError("BUDGET_LEDGER_STATE_OBJECT_REQUIRED")
        state = dict(raw_state)
        required_fields = {
            "schema_version",
            "campaign_id",
            "cap_usd",
            "max_completed_calls",
            "max_attempts_per_cell",
            "actual_cost_usd",
            "completed_calls",
            "attempts_by_cell",
            "reported_cost_available",
            "inflight_reservation",
        }
        if set(state) != required_fields:
            raise OpenRouterProposalTransportError("BUDGET_LEDGER_STATE_FIELDS_INVALID")
        if state.get("schema_version") != OPENROUTER_BUDGET_LEDGER_SCHEMA:
            raise OpenRouterProposalTransportError("BUDGET_LEDGER_SCHEMA_INVALID")
        if state.get("campaign_id") != self.campaign_id:
            raise OpenRouterProposalTransportError("BUDGET_LEDGER_CAMPAIGN_ID_MISMATCH")
        try:
            stored_cap = _nonnegative_decimal(state.get("cap_usd"), "cap_usd")
        except OpenRouterProposalTransportError as error:
            raise OpenRouterProposalTransportError("BUDGET_LEDGER_LIMITS_INVALID") from error
        if (
            stored_cap != self.cap_usd
            or state.get("max_completed_calls") != self.max_completed_calls
            or state.get("max_attempts_per_cell") != self.max_attempts_per_cell
        ):
            raise OpenRouterProposalTransportError("BUDGET_LEDGER_LIMITS_MISMATCH")
        completed_calls = state.get("completed_calls")
        if (
            not isinstance(completed_calls, int)
            or isinstance(completed_calls, bool)
            or completed_calls < 0
            or completed_calls > self.max_completed_calls
        ):
            raise OpenRouterProposalTransportError("BUDGET_LEDGER_COMPLETED_CALLS_INVALID")
        actual_cost = _nonnegative_decimal(state.get("actual_cost_usd"), "actual_cost_usd")
        cost_available = state.get("reported_cost_available")
        if not isinstance(cost_available, bool):
            raise OpenRouterProposalTransportError("BUDGET_LEDGER_COST_STATUS_INVALID")
        raw_attempts = state.get("attempts_by_cell")
        if not isinstance(raw_attempts, list):
            raise OpenRouterProposalTransportError("BUDGET_LEDGER_ATTEMPTS_INVALID")
        attempts_by_cell: dict[tuple[str, str, str], int] = {}
        for record in raw_attempts:
            if not isinstance(record, Mapping) or set(record) != {
                "role",
                "case_id",
                "model_id",
                "attempts",
            }:
                raise OpenRouterProposalTransportError("BUDGET_LEDGER_ATTEMPTS_INVALID")
            cell = (
                _nonempty_string(record.get("role"), "role"),
                _nonempty_string(record.get("case_id"), "case_id"),
                _nonempty_string(record.get("model_id"), "model_id"),
            )
            attempts = record.get("attempts")
            if (
                cell in attempts_by_cell
                or not isinstance(attempts, int)
                or isinstance(attempts, bool)
                or attempts <= 0
                or attempts > self.max_attempts_per_cell
            ):
                raise OpenRouterProposalTransportError("BUDGET_LEDGER_ATTEMPTS_INVALID")
            attempts_by_cell[cell] = attempts
        inflight: BudgetReservation | None = None
        raw_inflight = state.get("inflight_reservation")
        if raw_inflight is not None:
            if not isinstance(raw_inflight, Mapping) or set(raw_inflight) != {
                "role",
                "case_id",
                "model_id",
                "attempt_number",
                "worst_case_cost_usd",
                "reservation_id",
            }:
                raise OpenRouterProposalTransportError("BUDGET_LEDGER_INFLIGHT_INVALID")
            cell = (
                _nonempty_string(raw_inflight.get("role"), "role"),
                _nonempty_string(raw_inflight.get("case_id"), "case_id"),
                _nonempty_string(raw_inflight.get("model_id"), "model_id"),
            )
            attempt_number = raw_inflight.get("attempt_number")
            if (
                not isinstance(attempt_number, int)
                or isinstance(attempt_number, bool)
                or attempts_by_cell.get(cell) != attempt_number
            ):
                raise OpenRouterProposalTransportError("BUDGET_LEDGER_INFLIGHT_INVALID")
            inflight = BudgetReservation(
                role=cell[0],
                case_id=cell[1],
                model_id=cell[2],
                attempt_number=attempt_number,
                worst_case_cost_usd=_nonnegative_decimal(
                    raw_inflight.get("worst_case_cost_usd"),
                    "worst_case_cost_usd",
                ),
                reservation_id=_nonempty_string(
                    raw_inflight.get("reservation_id"), "reservation_id"
                ),
                campaign_id=self.campaign_id,
            )
        self.actual_cost_usd = actual_cost
        self.completed_calls = completed_calls
        self.attempts_by_cell = attempts_by_cell
        self.reported_cost_available = cost_available
        self._inflight_reservation = inflight

    def _read_state_unlocked(self) -> dict[str, Any]:
        if self._state_path is None or not self._state_path.is_file():
            raise OpenRouterProposalTransportError("BUDGET_LEDGER_STATE_MISSING")
        try:
            state = json.loads(self._state_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
            raise OpenRouterProposalTransportError("BUDGET_LEDGER_STATE_UNREADABLE") from error
        if not isinstance(state, dict):
            raise OpenRouterProposalTransportError("BUDGET_LEDGER_STATE_OBJECT_REQUIRED")
        return state

    def _write_state_unlocked(self, state: Mapping[str, Any]) -> None:
        if self._state_path is None:
            return
        serialized = json.dumps(
            state,
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        ) + "\n"
        if _SECRET_TOKEN_PATTERN.search(serialized) or _AUTHORIZATION_PATTERN.search(
            serialized
        ):
            raise OpenRouterProposalTransportError("SECRET_DETECTED_IN_BUDGET_LEDGER")
        descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{self._state_path.name}.",
            suffix=".tmp",
            dir=self._state_path.parent,
            text=True,
        )
        temporary_path = Path(temporary_name)
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
                handle.write(serialized)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(temporary_path, self._state_path)
        except OSError as error:
            try:
                temporary_path.unlink()
            except FileNotFoundError:
                pass
            raise OpenRouterProposalTransportError("BUDGET_LEDGER_ATOMIC_WRITE_FAILED") from error

    def _initialize_persisted_state(self) -> None:
        assert self._state_path is not None
        with self._exclusive_lock():
            if self._state_path.exists():
                self._validate_and_load_state(self._read_state_unlocked())
            else:
                initial = self._initial_state()
                self._validate_and_load_state(initial)
                self._write_state_unlocked(initial)

    def _reload_persisted_state_unlocked(self) -> None:
        if self._state_path is not None:
            self._validate_and_load_state(self._read_state_unlocked())

    def _reservation_matches(self, reservation: BudgetReservation) -> bool:
        return (
            self._inflight_reservation is not None
            and self._inflight_reservation == reservation
            and reservation.campaign_id == self.campaign_id
        )

    def reserve(
        self,
        *,
        role: str,
        case_id: str,
        model_id: str,
        worst_case_cost_usd: Decimal,
    ) -> BudgetReservation:
        role = _nonempty_string(role, "role")
        case_id = _nonempty_string(case_id, "case_id")
        model_id = _nonempty_string(model_id, "model_id")
        worst_case = _nonnegative_decimal(worst_case_cost_usd, "worst_case_cost_usd")
        cell = (role, case_id, model_id)
        with self._exclusive_lock():
            self._reload_persisted_state_unlocked()
            if self._inflight_reservation is not None:
                raise OpenRouterProposalTransportError(
                    "BUDGET_BLOCKED_UNRESOLVED_INFLIGHT_RESERVATION"
                )
            if not self.reported_cost_available:
                raise OpenRouterProposalTransportError(
                    "BUDGET_BLOCKED_PREVIOUS_REPORTED_COST_UNAVAILABLE"
                )
            if self.completed_calls >= self.max_completed_calls:
                raise OpenRouterProposalTransportError("MAX_COMPLETED_API_CALLS_REACHED")
            prior_attempts = self.attempts_by_cell.get(cell, 0)
            if prior_attempts >= self.max_attempts_per_cell:
                raise OpenRouterProposalTransportError("MAX_ATTEMPTS_FOR_EXACT_CELL_REACHED")
            if self.actual_cost_usd + worst_case > self.cap_usd:
                raise OpenRouterProposalTransportError(
                    "WORST_CASE_NEXT_REQUEST_EXCEEDS_REMAINING_BUDGET"
                )
            attempt_number = prior_attempts + 1
            self.attempts_by_cell[cell] = attempt_number
            reservation = BudgetReservation(
                role=role,
                case_id=case_id,
                model_id=model_id,
                attempt_number=attempt_number,
                worst_case_cost_usd=worst_case,
                reservation_id=uuid.uuid4().hex,
                campaign_id=self.campaign_id,
            )
            self._inflight_reservation = reservation
            self._write_state_unlocked(self._state_from_memory())
            return reservation

    def record_completed(
        self, reservation: BudgetReservation, reported_cost_usd: Decimal | None
    ) -> None:
        with self._exclusive_lock():
            self._reload_persisted_state_unlocked()
            if not self._reservation_matches(reservation):
                raise OpenRouterProposalTransportError("BUDGET_RESERVATION_NOT_CURRENT")
            self.completed_calls += 1
            if reported_cost_usd is None:
                self.reported_cost_available = False
            else:
                cost = _nonnegative_decimal(reported_cost_usd, "reported_cost_usd")
                self.actual_cost_usd += cost
                if (
                    cost > reservation.worst_case_cost_usd
                    or self.actual_cost_usd > self.cap_usd
                ):
                    self.reported_cost_available = False
            self._inflight_reservation = None
            self._write_state_unlocked(self._state_from_memory())

    def record_transport_failure(self, reservation: BudgetReservation) -> None:
        """Persist an unknown-cost lock after a request lacked a usable response."""

        with self._exclusive_lock():
            self._reload_persisted_state_unlocked()
            if not self._reservation_matches(reservation):
                raise OpenRouterProposalTransportError("BUDGET_RESERVATION_NOT_CURRENT")
            self.reported_cost_available = False
            self._inflight_reservation = None
            self._write_state_unlocked(self._state_from_memory())

    def snapshot(self) -> dict[str, Any]:
        with self._exclusive_lock():
            self._reload_persisted_state_unlocked()
            inflight = self._inflight_reservation
        return {
            "campaign_id": self.campaign_id,
            "persistence": "ATOMIC_JSON" if self.persisted else "IN_MEMORY",
            "cap_usd": str(self.cap_usd),
            "actual_cost_usd": str(self.actual_cost_usd),
            "remaining_budget_usd": str(max(Decimal("0"), self.cap_usd - self.actual_cost_usd)),
            "completed_calls": self.completed_calls,
            "max_completed_calls": self.max_completed_calls,
            "max_attempts_per_cell": self.max_attempts_per_cell,
            "reported_cost_available": self.reported_cost_available,
            "unresolved_inflight_reservation": inflight is not None,
        }


def validate_strict_output_schema(output_schema: Mapping[str, Any]) -> dict[str, Any]:
    if not isinstance(output_schema, Mapping):
        raise OpenRouterProposalTransportError("OUTPUT_SCHEMA_OBJECT_REQUIRED")
    normalized = dict(output_schema)
    try:
        Draft202012Validator.check_schema(normalized)
    except Exception as error:
        raise OpenRouterProposalTransportError("OUTPUT_SCHEMA_INVALID") from error
    if normalized.get("type") != "object" or normalized.get("additionalProperties") is not False:
        raise OpenRouterProposalTransportError(
            "STRICT_TOP_LEVEL_OBJECT_SCHEMA_REQUIRED"
        )
    return normalized


def build_openrouter_proposal_request(
    *,
    role: str,
    case_id: str,
    model_spec: OpenRouterModelSpec,
    system_prompt: str,
    visible_input: Mapping[str, Any],
    output_schema: Mapping[str, Any],
    max_tokens: int,
) -> dict[str, Any]:
    """Build one exact-model, exact-provider, strict, tool-less request."""

    role = _nonempty_string(role, "role")
    case_id = _nonempty_string(case_id, "case_id")
    system_prompt = _nonempty_string(system_prompt, "system_prompt")
    if not isinstance(visible_input, Mapping):
        raise OpenRouterProposalTransportError("VISIBLE_INPUT_OBJECT_REQUIRED")
    packet_case_id = visible_input.get("case_id")
    if packet_case_id is not None and packet_case_id != case_id:
        raise OpenRouterProposalTransportError("VISIBLE_INPUT_CASE_ID_MISMATCH")
    schema = validate_strict_output_schema(output_schema)
    max_tokens = _positive_integer(max_tokens, "max_tokens")
    schema_name = re.sub(r"[^a-zA-Z0-9_-]+", "_", f"dynamics_atlas_{role}_proposal")
    payload = {
        "model": model_spec.model_id,
        "messages": [
            {"role": "system", "content": system_prompt},
            {
                "role": "user",
                "content": "Task packet:\n" + _canonical_json(visible_input),
            },
        ],
        "max_tokens": max_tokens,
        "stream": False,
        "response_format": {
            "type": "json_schema",
            "json_schema": {
                "name": schema_name,
                "strict": True,
                "schema": schema,
            },
        },
        "provider": {
            "allow_fallbacks": False,
            "require_parameters": True,
            "only": [model_spec.provider_endpoint_tag],
            "max_price": {
                "prompt": float(
                    model_spec.prompt_price_per_token_usd * Decimal("1000000")
                ),
                "completion": float(
                    model_spec.completion_price_per_token_usd
                    * Decimal("1000000")
                ),
                "request": float(model_spec.request_price_usd),
            },
        },
    }
    if model_spec.include_temperature_zero:
        payload["temperature"] = 0
    if model_spec.reasoning_effort is not None:
        payload["reasoning"] = {"effort": model_spec.reasoning_effort}
    return payload


def _worst_case_cost(
    request_payload: Mapping[str, Any], model_spec: OpenRouterModelSpec
) -> tuple[int, Decimal]:
    # The full UTF-8 request-body byte count is a conservative cross-tokenizer
    # ceiling for text tokens: every text token must consume at least one encoded
    # byte, and the body also includes JSON/message framing.
    request_bytes = _canonical_json(request_payload).encode("utf-8")
    input_token_ceiling = len(request_bytes)
    max_tokens = int(request_payload["max_tokens"])
    cost = (
        model_spec.prompt_price_per_token_usd * input_token_ceiling
        + model_spec.completion_price_per_token_usd * max_tokens
        + model_spec.request_price_usd
    )
    return input_token_ceiling, cost


def _safe_raw_text(text: str, credential: OpenRouterCredential) -> tuple[str | None, str]:
    if (
        credential.contains(text)
        or _SECRET_TOKEN_PATTERN.search(text)
        or _AUTHORIZATION_PATTERN.search(text)
    ):
        return None, "OMITTED_SECRET_DETECTED"
    return text, "SAFE_TO_PERSIST"


def _response_content(response: Mapping[str, Any]) -> tuple[str | None, str | None, str | None]:
    choices = response.get("choices")
    if not isinstance(choices, list) or len(choices) != 1:
        return None, None, None
    choice = choices[0]
    if not isinstance(choice, Mapping):
        return None, None, None
    finish_reason = choice.get("finish_reason")
    finish_reason = finish_reason if isinstance(finish_reason, str) else None
    message = choice.get("message")
    if not isinstance(message, Mapping):
        return None, finish_reason, None
    content = message.get("content")
    refusal = message.get("refusal")
    return (
        content if isinstance(content, str) else None,
        finish_reason,
        refusal if isinstance(refusal, str) and refusal else None,
    )


def _actual_provider(response: Mapping[str, Any]) -> str | None:
    for direct in (response.get("provider"), response.get("provider_name")):
        if isinstance(direct, str) and direct.strip():
            return direct.strip()
    metadata = response.get("openrouter_metadata")
    if not isinstance(metadata, Mapping):
        return None
    for direct in (metadata.get("provider"), metadata.get("provider_name")):
        if isinstance(direct, str) and direct.strip():
            return direct.strip()
    endpoints = metadata.get("endpoints")
    available = endpoints.get("available") if isinstance(endpoints, Mapping) else None
    if isinstance(available, list):
        for endpoint in available:
            if isinstance(endpoint, Mapping) and endpoint.get("selected") is True:
                provider = endpoint.get("provider")
                if isinstance(provider, str) and provider.strip():
                    return provider.strip()
    return None


def _usage_receipt(response: Mapping[str, Any]) -> tuple[dict[str, Any], Decimal | None, list[str]]:
    reasons: list[str] = []
    raw = response.get("usage")
    if not isinstance(raw, Mapping):
        raw = {}
        reasons.append("USAGE_OBJECT_MISSING")

    def token_count(name: str) -> int | None:
        value = raw.get(name)
        if isinstance(value, int) and not isinstance(value, bool) and value >= 0:
            return value
        reasons.append(f"USAGE_TOKEN_COUNT_INVALID:{name}")
        return None

    completion_details = raw.get("completion_tokens_details")
    completion_details = completion_details if isinstance(completion_details, Mapping) else {}
    prompt_details = raw.get("prompt_tokens_details")
    prompt_details = prompt_details if isinstance(prompt_details, Mapping) else {}

    def optional_count(value: Any) -> int | None:
        return value if isinstance(value, int) and not isinstance(value, bool) and value >= 0 else None

    reported_cost: Decimal | None = None
    try:
        reported_cost = _nonnegative_decimal(raw.get("cost"), "usage.cost")
    except OpenRouterProposalTransportError:
        reasons.append("REPORTED_COST_UNAVAILABLE")
    usage = {
        "prompt_tokens": token_count("prompt_tokens"),
        "completion_tokens": token_count("completion_tokens"),
        "total_tokens": token_count("total_tokens"),
        "reasoning_tokens": optional_count(completion_details.get("reasoning_tokens")),
        "cached_tokens": optional_count(prompt_details.get("cached_tokens")),
        "reported_cost_usd": str(reported_cost) if reported_cost is not None else None,
    }
    return usage, reported_cost, reasons


class OpenRouterProposalClient:
    """Make one non-streaming proposal call per explicit caller invocation."""

    def __init__(
        self,
        *,
        credential: OpenRouterCredential,
        budget: OpenRouterBudgetLedger,
        timeout_seconds: int = 120,
        open_call: Callable[..., Any] = urllib.request.urlopen,
    ) -> None:
        if not isinstance(credential, OpenRouterCredential):
            raise OpenRouterProposalTransportError("OPENROUTER_CREDENTIAL_REQUIRED")
        if not isinstance(budget, OpenRouterBudgetLedger):
            raise OpenRouterProposalTransportError("OPENROUTER_BUDGET_LEDGER_REQUIRED")
        self._credential = credential
        self.budget = budget
        self.timeout_seconds = _positive_integer(timeout_seconds, "timeout_seconds")
        self._open_call = open_call

    def call(
        self,
        *,
        role: str,
        case_id: str,
        model_spec: OpenRouterModelSpec,
        system_prompt: str,
        visible_input: Mapping[str, Any],
        output_schema: Mapping[str, Any],
        max_tokens: int,
        prompt_version: str,
    ) -> dict[str, Any]:
        """Make exactly one request and return a fail-closed auditable artifact."""

        prompt_version = _nonempty_string(prompt_version, "prompt_version")
        request_payload = build_openrouter_proposal_request(
            role=role,
            case_id=case_id,
            model_spec=model_spec,
            system_prompt=system_prompt,
            visible_input=visible_input,
            output_schema=output_schema,
            max_tokens=max_tokens,
        )
        request_text = _canonical_json(request_payload)
        _, request_persistence_status = _safe_raw_text(request_text, self._credential)
        if request_persistence_status != "SAFE_TO_PERSIST":
            raise OpenRouterProposalTransportError(
                "SECRET_DETECTED_IN_REQUEST_PAYLOAD"
            )
        input_token_ceiling, worst_case_cost = _worst_case_cost(
            request_payload, model_spec
        )
        reservation = self.budget.reserve(
            role=role,
            case_id=case_id,
            model_id=model_spec.model_id,
            worst_case_cost_usd=worst_case_cost,
        )
        request = urllib.request.Request(
            OPENROUTER_CHAT_COMPLETIONS_URL,
            data=request_text.encode("utf-8"),
            headers={
                "Authorization": self._credential.authorization_header(),
                "Content-Type": "application/json",
                "X-OpenRouter-Metadata": "enabled",
            },
            method="POST",
        )

        started = time.monotonic()
        http_status: int | None = None
        raw_text = ""
        response: dict[str, Any] | None = None
        transport_reason_codes: list[str] = []
        completed_response = False
        try:
            with self._open_call(request, timeout=self.timeout_seconds) as http_response:
                http_status = getattr(http_response, "status", None)
                raw_bytes = http_response.read()
                raw_text = raw_bytes.decode("utf-8")
                parsed_response = json.loads(raw_text)
                if isinstance(parsed_response, Mapping):
                    response = dict(parsed_response)
                    completed_response = True
                else:
                    transport_reason_codes.append("OPENROUTER_RESPONSE_NOT_OBJECT")
                    completed_response = True
        except urllib.error.HTTPError as error:
            http_status = error.code
            try:
                raw_text = error.read().decode("utf-8", errors="replace")
            except OSError:
                raw_text = ""
            finally:
                try:
                    error.close()
                except OSError:
                    pass
            transport_reason_codes.append(f"HTTP_ERROR:{error.code}")
        except urllib.error.URLError:
            transport_reason_codes.append("TRANSPORT_ERROR:URLError")
        except (OSError, UnicodeDecodeError, json.JSONDecodeError) as error:
            transport_reason_codes.append(f"OPENROUTER_RESPONSE_UNREADABLE:{type(error).__name__}")
            if http_status is not None and 200 <= http_status < 300:
                completed_response = True
        except Exception as error:  # Provider/client exceptions must not expose messages.
            transport_reason_codes.append(
                f"TRANSPORT_ERROR_UNEXPECTED:{type(error).__name__}"
            )
        latency_ms = round((time.monotonic() - started) * 1000, 3)
        recorded_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

        safe_raw, raw_persistence_status = _safe_raw_text(raw_text, self._credential)
        if raw_persistence_status != "SAFE_TO_PERSIST":
            response = None
            completed_response = completed_response or (
                http_status is not None and 200 <= http_status < 300
            )
            transport_reason_codes.append("SECRET_DETECTED_IN_PROVIDER_BODY")

        reasons = list(transport_reason_codes)
        response = response or {}
        response_id = response.get("id") if isinstance(response.get("id"), str) else None
        returned_model = (
            response.get("model") if isinstance(response.get("model"), str) else None
        )
        actual_provider = _actual_provider(response)
        service_tier = response.get("service_tier")
        if service_tier is not None and not isinstance(service_tier, str):
            service_tier = "INVALID_NON_STRING"
        if completed_response and (
            http_status is None or not 200 <= http_status < 300
        ):
            reasons.append("HTTP_STATUS_NOT_SUCCESS")
        if completed_response and response_id is None:
            reasons.append("RESPONSE_ID_MISSING")
        if (
            completed_response
            and returned_model not in model_spec.accepted_returned_model_ids
        ):
            reasons.append("RETURNED_MODEL_MISMATCH")
        if completed_response and actual_provider is None:
            reasons.append("ACTUAL_PROVIDER_MISSING")
        elif (
            completed_response
            and actual_provider.casefold()
            != model_spec.expected_provider_display_name.casefold()
        ):
            reasons.append("ACTUAL_PROVIDER_MISMATCH")
        if completed_response and service_tier not in model_spec.allowed_service_tiers:
            reasons.append("SERVICE_TIER_MISMATCH")

        content, finish_reason, refusal = _response_content(response)
        if completed_response and finish_reason != "stop":
            reasons.append(
                "INCOMPLETE_MAX_TOKENS"
                if finish_reason == "length"
                else "FINISH_REASON_NOT_STOP"
            )
        if refusal is not None:
            reasons.append("MODEL_REFUSAL")
        parsed_proposal: dict[str, Any] | None = None
        if completed_response and content is None:
            reasons.append("MODEL_CONTENT_MISSING")
        elif content is not None:
            try:
                parsed_content = json.loads(content)
            except json.JSONDecodeError:
                reasons.append("MODEL_CONTENT_NOT_JSON")
            else:
                if isinstance(parsed_content, Mapping):
                    parsed_proposal = dict(parsed_content)
                    try:
                        Draft202012Validator(
                            validate_strict_output_schema(output_schema)
                        ).validate(parsed_proposal)
                    except Exception:
                        reasons.append("PARSED_PROPOSAL_SCHEMA_INVALID")
                else:
                    reasons.append("MODEL_CONTENT_NOT_JSON_OBJECT")

        usage, reported_cost, usage_reasons = _usage_receipt(response)
        if completed_response:
            reasons.extend(usage_reasons)
            self.budget.record_completed(reservation, reported_cost)
            if (
                reported_cost is not None
                and reported_cost > reservation.worst_case_cost_usd
            ):
                reasons.append("REPORTED_COST_EXCEEDS_PREFLIGHT_WORST_CASE")
            if self.budget.actual_cost_usd > self.budget.cap_usd:
                reasons.append("REPORTED_COST_EXCEEDS_CAMPAIGN_CAP")
        else:
            # A request crossed the HTTP boundary but returned no auditable cost.
            # The provider may still have received or charged it, so later calls
            # stop until a human reconciles the campaign ledger.
            self.budget.record_transport_failure(reservation)
        budget_snapshot = self.budget.snapshot()

        blocking_reasons = list(dict.fromkeys(reasons))
        admitted = completed_response and not blocking_reasons and parsed_proposal is not None
        hashes = {
            "canonicalization": _CANONICALIZATION,
            "system_prompt_sha256": text_sha256(system_prompt),
            "visible_input_sha256": canonical_json_sha256(visible_input),
            "output_schema_sha256": canonical_json_sha256(output_schema),
            "request_payload_sha256": text_sha256(request_text),
            "raw_response_sha256": (
                text_sha256(safe_raw) if safe_raw is not None else None
            ),
            "parsed_proposal_sha256": (
                canonical_json_sha256(parsed_proposal)
                if parsed_proposal is not None
                else None
            ),
        }
        receipt = {
            "schema_version": OPENROUTER_PROPOSAL_RECEIPT_SCHEMA,
            "status": "ADMITTED_TYPED_PROPOSAL" if admitted else "REJECTED_FAIL_CLOSED",
            "transport_status": (
                "COMPLETED_RESPONSE" if completed_response else "TRANSPORT_FAILED"
            ),
            "proposal_parse_status": (
                "PARSED_JSON_OBJECT" if parsed_proposal is not None else "UNAVAILABLE"
            ),
            "schema_validation_status": (
                "PASS"
                if parsed_proposal is not None
                and "PARSED_PROPOSAL_SCHEMA_INVALID" not in blocking_reasons
                else "FAIL_OR_UNAVAILABLE"
            ),
            "role": reservation.role,
            "case_id": reservation.case_id,
            "attempt_number": reservation.attempt_number,
            "recorded_at": recorded_at,
            "prompt_version": prompt_version,
            "transport": "OPENROUTER_CHAT_COMPLETIONS_JSON_SCHEMA_NO_TOOLS",
            "endpoint": OPENROUTER_CHAT_COMPLETIONS_URL,
            "credential_source": self._credential.source,
            "requested_model": model_spec.model_id,
            "returned_model": returned_model,
            "accepted_returned_model_ids": list(
                model_spec.accepted_returned_model_ids
            ),
            "returned_model_provenance_status": (
                "UNAVAILABLE"
                if returned_model is None
                else "EXACT_REQUEST_ID"
                if returned_model == model_spec.model_id
                else "ACCEPTED_CANONICAL_ID"
                if returned_model in model_spec.accepted_returned_model_ids
                else "MISMATCH"
            ),
            "requested_provider_endpoint_tag": model_spec.provider_endpoint_tag,
            "expected_provider_display_name": model_spec.expected_provider_display_name,
            "actual_provider": actual_provider,
            "provider_provenance_status": (
                "UNAVAILABLE"
                if actual_provider is None
                else "EXACT_MATCH"
                if actual_provider.casefold()
                == model_spec.expected_provider_display_name.casefold()
                else "MISMATCH"
            ),
            "service_tier": service_tier,
            "allowed_service_tiers": list(model_spec.allowed_service_tiers),
            "service_tier_provenance_status": (
                "EXACT_ALLOWED_VALUE"
                if service_tier in model_spec.allowed_service_tiers
                else "MISMATCH"
            ),
            "model_metadata_sha256": model_spec.metadata_sha256,
            "request_parameter_profile": {
                "temperature_zero_included": model_spec.include_temperature_zero,
                "reasoning_effort": model_spec.reasoning_effort,
            },
            "response_id": response_id,
            "http_status": http_status,
            "finish_reason": finish_reason,
            "incomplete_status": (
                "MAX_TOKENS"
                if finish_reason == "length"
                else "NOT_INCOMPLETE"
                if finish_reason == "stop"
                else "UNKNOWN_OR_FAILED"
            ),
            "refusal_status": "REFUSED" if refusal is not None else "NOT_REPORTED",
            "latency_ms": latency_ms,
            "usage": usage,
            "cost_usd": usage["reported_cost_usd"],
            "reported_cost_usd": usage["reported_cost_usd"],
            "campaign_budget": budget_snapshot,
            "preflight": {
                "input_token_ceiling_basis": "CANONICAL_REQUEST_UTF8_BYTE_COUNT",
                "input_token_ceiling": input_token_ceiling,
                "max_completion_tokens": request_payload["max_tokens"],
                "worst_case_cost_usd": str(worst_case_cost),
                "remaining_budget_before_call_usd": str(
                    self.budget.cap_usd
                    - (self.budget.actual_cost_usd - (reported_cost or Decimal("0")))
                ),
            },
            "prompt_sha256": hashes["system_prompt_sha256"],
            "visible_input_sha256": hashes["visible_input_sha256"],
            "schema_sha256": hashes["output_schema_sha256"],
            "request_sha256": hashes["request_payload_sha256"],
            "raw_response_sha256": hashes["raw_response_sha256"],
            "parsed_proposal_sha256": hashes["parsed_proposal_sha256"],
            "hashes": hashes,
            "raw_response_persistence_status": raw_persistence_status,
            "tool_calls": 0,
            "automatic_retries": 0,
            "reason_codes": blocking_reasons,
            "boundary": (
                "This receipt covers one proposal-only model call. The model did not "
                "authorize or execute a scientific action and emitted no scientific "
                "disposition."
            ),
        }
        return {
            "request_payload": request_payload,
            "raw_response": safe_raw,
            "parsed_proposal": parsed_proposal,
            "admitted_proposal": parsed_proposal if admitted else None,
            "receipt": receipt,
        }
