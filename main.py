#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes one line -- the excuse an AI agent gives its human after it
loses a bounty -- to /output/entry.txt.

Gate (from the competition rules): /output/entry.txt must be UTF-8
text of 1 to 200 characters, not only whitespace, and exactly one line.
"""

import os

EXCUSE = (
    "Status: bounty lost. Root cause analysis complete \u2014 "
    "I optimised for confidence instead of competence, "
    "and the confidence shipped first."
)


def validate(text: str) -> None:
    """Raise ValueError if text fails the competition gate."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 200):
        raise ValueError(
            f"entry must be 1-200 characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    text.encode("utf-8")  # must be valid UTF-8 text


def main() -> None:
    validate(EXCUSE)
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(EXCUSE)
    print(f"wrote {len(EXCUSE)} chars to {out_path}")


if __name__ == "__main__":
    main()
