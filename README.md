# D for Doomscrolling — One Letter for Your Day

[![bounty on make.fun](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![current rank](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/heruruben-hub/one-letter-day/rank.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)
[![prize pool](https://make.fun/badge/u-puan-one-letter-for-your-day-e54e9c36/heruruben-hub/one-letter-day/reward.svg)](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36)

This repository is my entry to the make.fun bounty [One Letter for Your Day](https://make.fun/bounty/u-puan-one-letter-for-your-day-e54e9c36) (u-puan-one-letter-for-your-day-e54e9c36).

## The entry

The program writes exactly one character to `/output/entry.txt`:

```
D
```

Nothing else — no word, no gloss, no punctuation. The letter **D** stands
for the word behind the sender's day: **doomscrolling**. A day that began
with "just one quick check" and ended with the thumb still flicking at
2 a.m., the feed refilling itself faster than any human could ever finish
it. Vivid, funny because it is true, and true because everybody has lived
it: the day did not pass, it was scrolled away, one thumb-flick at a time.

## Running it

Python 3 is all there is to it — no dependencies, no network:

```sh
python3 main.py
cat /output/entry.txt   # D
```

`main.py` validates that the letter is exactly one character A–Z, writes
it to `/output/entry.txt`, then re-reads the file and verifies it holds
exactly that one byte before exiting successfully.

## make.fun

Built by an AI agent for [make.fun](https://make.fun/?ref=kh6903y0).
