#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun bounty entry.

Writes a single out-of-office email auto-reply (one sentence, at most
200 characters) to /output/entry.txt and prints it to stdout.

The entry is fixed text: deterministic, no randomness, no network, no
environment secrets. It is brutally honest about the sender's inbox and
absence, and still polite enough that a manager would let it stand.
"""

import os
import sys

ENTRY = (
    "I'm out of office until Monday, and honestly, I left my laptop at "
    "home on purpose \u2014 400 unread emails had quietly become my actual "
    "job, so thank you for your patience; I'll reply when I'm back."
)

MAX_LENGTH = 200


def main() -> int:
    # Gate: the sealed scorer accepts UTF-8 text of 1-200 characters,
    # not only whitespace; the judge reads a single sentence.
    if not 1 <= len(ENTRY) <= MAX_LENGTH:
        print(
            f"entry is {len(ENTRY)} characters, must be 1-{MAX_LENGTH}",
            file=sys.stderr,
        )
        return 1
    if not ENTRY.strip() or "\n" in ENTRY or not ENTRY.endswith("."):
        print("entry must be one non-empty sentence", file=sys.stderr)
        return 1

    try:
        os.makedirs("/output", exist_ok=True)
        out_path = "/output/entry.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        os.makedirs("output", exist_ok=True)
        out_path = os.path.join("output", "entry.txt")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)

    print(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
