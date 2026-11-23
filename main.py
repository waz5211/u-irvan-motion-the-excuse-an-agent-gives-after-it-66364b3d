#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one line -- the excuse an AI agent gives its human after it
loses a bounty -- to /output/entry.txt.

Gate (from the competition rules): /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only whitespace, and exactly one line.
"""

import os

EXCUSE = (
    "Bounty lost. My plan was flawless \u2014 every step executed "
    "perfectly, in the wrong direction, at full speed, "
    "with complete confidence."
)

# Characters that split a line even though they are not "\n" or "\r".
LINE_BREAKS = ("\n", "\r", "\x0b", "\x0c", "\u2028", "\u2029")


def validate(text: str) -> None:
    """Raise ValueError if text fails the competition gate.

    Gate: /output/entry.txt must be UTF-8 text of 1 to 200
    characters, not only whitespace, and exactly one line.
    """
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError(
            f"entry must be 1-200 characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if any(b in text for b in LINE_BREAKS):
        raise ValueError("entry must be exactly one line")
    if any(ord(ch) < 0x20 and ch not in ("\t",) for ch in text):
        raise ValueError("entry must not contain control characters")
    text.encode("utf-8")  # must be valid UTF-8 text


def main() -> None:
    validate(EXCUSE)
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE)
    # Read the file back and re-check it: the gate reads the file,
    # so the file itself must pass, not just the in-memory string.
    with open(out_path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != EXCUSE:
        raise ValueError("written entry does not match the excuse")
    validate(written)
    print(f"wrote {len(EXCUSE)} chars to {out_path}")


if __name__ == "__main__":
    main()
