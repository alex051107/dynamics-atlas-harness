"""The one DOI key every pipeline step uses. Import doi_key from here; do not write another normalizer.

Past mistakes this owns (2026-11-11): five copies spelled DOIs differently, so old Wiley SICI DOIs with < > were
rejected at merge (5 entries failed), URL-encoded seeds (%2b, %3c) were encoded again for OpenAlex and the seed lookup
failed (CBFB, BARSTAR), and one paper sat in a candidate list twice under two spellings. tests/test_doi_key.py holds
those DOIs as fixtures.
"""
import os
import html
import re
from urllib.parse import unquote

# Validates a whole DOI. Allows < > because SICI DOIs contain them; finding DOIs inside prose is a different job
# (edison_candidates.DOI_PATTERN stops at < > there, on purpose).
DOI_KEY_PATTERN = re.compile(r"10\.\d{4,9}/[^\s\"'\[\]{}\\?#`*，。；：！？⺀-￯]+", re.IGNORECASE)
URL_SUFFIX = re.compile(r"(?:\.full\.pdf|\.full|\.pdf|/pdf|/epdf|/full|/abstract|/download)$", re.IGNORECASE)


def doi_key(value):
    """Lower-case bare DOI, decoded, without resolver prefix or trailing punctuation; '' when it is not a DOI."""
    if not isinstance(value, str):
        return ""
    text = html.unescape(unquote(value.strip()))
    text = re.sub(r"^(?:https?://(?:dx\.)?doi\.org/|doi:\s*)", "", text, flags=re.IGNORECASE)
    text = text.rstrip(".,;:!?，。；：！")
    while text.endswith(")") and text.count(")") > text.count("("):
        text = text[:-1].rstrip(".,;:")
    text = URL_SUFFIX.sub("", text)  # a publisher URL form (".pdf", "/full", "/download") names the same paper
    return text.lower() if DOI_KEY_PATTERN.fullmatch(text) else ""
