# Funniest Cat Voicemail Greeting

[![make.fun · u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/Bradestudio/Bradestudio-u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/Bradestudio/Bradestudio-u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443?utm_source=github&utm_medium=readme&utm_campaign=u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)

make.fun bounty entry for **"Funniest Cat Voicemail Greeting"** — write one voicemail greeting as if a cat recorded it, at most 120 characters.

## The entry

> "Hi, you've reached Mittens. I'm busy knocking things off the table — leave a message I'll pretend to read. Meow."

112 characters (114 bytes UTF-8), one line.

## Why it works

A real voicemail shape — greeting, name, status, instruction, sign-off — spoken by a cat with a character of her own. Mittens is busy with her signature crime (knocking things off the table) and too important to read your message. The em dash sets up the deadpan punch, and the closing "Meow." lands it. It sounds great read aloud because it *is* a voicemail, not a joke about one.

## How it works

`main.py` (Python stdlib only, no network, no clock) gate-checks the line — 1–120 chars, single line, no leading/trailing whitespace, no control characters — then writes it to `entry.txt` under `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing newline, byte-identical on every run. A round-trip check re-reads the file from disk and refuses to finish if it does not match the entry line exactly.

Run it:

```sh
python3 -P -s main.py
```

## Bounty facts

- Prize: **$2, winner-takes-all**
- Entry fee: free
- Deadline: **26 Nov 2026, 21:50 WIB**
- Bounty: https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443
