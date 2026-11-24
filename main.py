#!/usr/bin/env python3
"""The Most Honest Outage Line - make.fun bounty entry.

Writes a single status page line (at most 160 characters) to
/output/entry.txt, then reads it back and asserts the round-trip
matches exactly. Standard library only.
"""

import os

ENTRY = (
    "All servers are down, including the monitors that would tell me why. "
    "I can't check if I'm still running, or when we'll be back. "
    "This page is all that's left."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 160, f"entry is {len(ENTRY)} chars, must be 1-160"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY and ENTRY == ENTRY.strip(), (
        "entry must be a single line with no leading/trailing whitespace"
    )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    # Round-trip assert: read it back and verify content + char count.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == ENTRY, "round-trip mismatch"
    assert 1 <= len(back) <= 160, f"round-trip entry is {len(back)} chars"
    print(f"Wrote {len(back)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
