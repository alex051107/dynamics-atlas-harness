"""Linux sandbox for the agent's `python` tool and POTENCI (macOS keeps using sandbox-exec).

bubblewrap: no network, filesystem limited to the read-only system dirs, the interpreter's
prefixes, the read-only paths asked for and the writable paths asked for. If bwrap is missing
the caller gets an error; there is no unsandboxed fallback.
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path


def bwrap_cmd(argv: list[str], ro: list[Path], rw: list[Path], cwd: Path) -> list[str]:
    exe = shutil.which("bwrap")
    if not exe:
        raise FileNotFoundError("bwrap (bubblewrap) not found; refusing to run unsandboxed")
    cmd = [exe, "--die-with-parent", "--unshare-net", "--unshare-pid", "--unshare-ipc", "--unshare-uts",
           "--ro-bind", "/usr", "/usr", "--ro-bind", "/etc", "/etc",
           "--symlink", "usr/lib", "/lib", "--symlink", "usr/lib64", "/lib64", "--symlink", "usr/bin", "/bin",
           "--symlink", "usr/sbin", "/sbin", "--proc", "/proc", "--dev", "/dev", "--tmpfs", "/tmp"]
    seen: set[str] = set()
    for p in [Path(sys.prefix), Path(sys.base_prefix), Path(sys.executable).resolve().parent.parent, *ro]:
        s = str(p.resolve())
        if s not in seen:
            seen.add(s)
            cmd += ["--ro-bind", s, s]
    for p in rw:
        s = str(p.resolve())
        cmd += ["--bind", s, s]
    return cmd + ["--chdir", str(cwd.resolve()), "--", *argv]
