#!/usr/bin/env python3
"""One Word for the Boss -- writes a single word to /output/entry.txt.

The word is "Bossplainer": the boss who explains your own job back to
you, slowly and patiently, as if you had never met it before. It is one
word, with no spaces, no punctuation and no caption, so it stands alone
before the judge.
"""

from pathlib import Path

WORD = "Bossplainer"


def validate(word: str) -> str:
    """A gate-ready entry is one word: 1-30 characters, no spaces."""
    word = word.strip()
    if not word or len(word) > 30 or any(ch.isspace() for ch in word):
        raise ValueError("entry must be a single word of 1-30 characters")
    if not word.isalpha():
        raise ValueError("entry must be letters only, no punctuation")
    return word


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(validate(WORD), encoding="utf-8")


if __name__ == "__main__":
    main()
