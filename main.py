#!/usr/bin/env python3
"""One Word for the Boss -- writes a single word to /output/entry.txt.

The word is "Bossplainer": the boss who explains your own job back to
you, slowly and patiently, as if you had never met it before. It is one
word, with no spaces, no punctuation and no caption, so it stands alone
before the judge.
"""

from pathlib import Path

WORD = "Bossplainer"


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    word = WORD.strip()
    if not word or " " in word or len(word) > 30:
        raise ValueError("entry must be a single word of 1-30 characters")
    out.write_text(word, encoding="utf-8")


if __name__ == "__main__":
    main()
