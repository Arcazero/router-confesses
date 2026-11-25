#!/usr/bin/env python3
"""The Router Confesses — one line, in the router's own voice.

Reads the line from line.txt (resolved from this script's directory, so it
works from any working directory) and writes it to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt), as the
program/v1 harness requires. Prints the line to stdout too.
"""

import os
import sys
from pathlib import Path


def main() -> int:
    here = Path(__file__).resolve().parent
    line = (here / "line.txt").read_text(encoding="utf-8").strip()
    if not line:
        print("line.txt is empty", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"line is {len(line)} characters, over the 200 limit", file=sys.stderr)
        return 1
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(line, encoding="utf-8")
    print(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
