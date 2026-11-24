"""Alien Field Notes: The Two Day Earth Review.

Writes the entry line -- one original review of planet Earth by an alien
tourist, at most 200 characters -- to /output/entry.txt (or
MAKEFUN_OUTPUT_DIR when the grader sets it).

Stdlib only: no imports beyond the standard library, no network, no
environment secrets. The line is a constant in this file.
"""

import os
import sys

ENTRY = (
    "Day 2: the locals apologise to their cleaning robots, thank the cash "
    "machines, and wave at neighbours they pray won't stop to chat. "
    "Four stars \u2014 would abduct again."
)


def main() -> int:
    text = ENTRY.strip()
    if not text or len(text) > 200:
        print(f"entry invalid: {len(text)} characters", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry invalid: must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
