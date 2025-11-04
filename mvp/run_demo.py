#!/usr/bin/env python3

"""Execute the MVP compiler against the bundled sample program."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parent
    compiler = root / "llmpl_to_python.py"
    source = root / "example_mvp.llmpl"

    result = subprocess.run(
        [sys.executable, str(compiler), str(source), "--run"],
        cwd=root,
        check=False,
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
