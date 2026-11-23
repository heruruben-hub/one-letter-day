#!/usr/bin/env python3
"""One Letter for Your Day — "D" for doomscrolling.

Entry for the make.fun bounty "One Letter for Your Day"
(u-puan-one-letter-for-your-day-e54e9c36).

The program writes exactly one character, the letter D, to
/output/entry.txt — nothing else: no word, no gloss, no punctuation.

The letter stands for the word behind the sender's day: doomscrolling.
A day that began with "just one quick check" and ended with the thumb
still flicking at 2 a.m., the newsfeed refilling itself faster than any
human could ever finish it. Vivid, funny because it is true, and true
because everybody has lived it: the day did not pass, it was scrolled
away, one thumb-flick at a time.

After writing, the program re-reads the file and verifies it holds
exactly that one byte before exiting successfully.
"""

import os
import sys

# The entry: one letter, A-Z. D for doomscrolling.
#
# Why D, and why doomscrolling: the word behind the letter is the whole
# entry, so it has to land at once. Doomscrolling is the day that never
# happened — it began with "just one quick check" and ended with the
# thumb still flicking at 2 a.m., the feed refilling itself faster than
# any human could ever finish it. It is vivid (the glow of the screen in
# a dark room), funny because it is true, and true because everybody has
# lived it. D is also the shape of the day: a half-finished circle, the
# loop that never closes. No other single letter carries a day like that.
LETTER = "D"

# The full alphabet the gate accepts, as an explicit set rather than a
# range comparison, so the validation says exactly what it allows.
VALID_LETTERS = frozenset("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


def main() -> int:
    if len(LETTER) != 1 or LETTER not in VALID_LETTERS:
        print(
            f"entry letter must be exactly one character A-Z; "
            f"got {LETTER!r} (length {len(LETTER)})",
            file=sys.stderr,
        )
        return 1

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)

    # Verify: re-read and check the file holds exactly that one byte.
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    if data != LETTER.encode("ascii"):
        print(f"verification failed: entry.txt holds {data!r}",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
