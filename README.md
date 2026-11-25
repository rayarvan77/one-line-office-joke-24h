# One-Line Office Joke: 24-Hour Sprint

[![make.fun · u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![rank](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/rayarvan77/one-line-office-joke-24h/rank.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)
[![reward](https://make.fun/badge/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162/rayarvan77/one-line-office-joke-24h/reward.svg)](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)

An entry for the [make.fun](https://make.fun) bounty
[One-Line Office Joke: 24-Hour Sprint](https://make.fun/bounty/u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162).

## The joke

> Our office plant has outlasted four managers and two restructures, so HR gave it a parking space and a pension plan.

One sentence, 116 characters — comfortably inside the bounty gate of
1 to 200 characters. The setup names the most durable employee in any
office (the plant nobody waters and nobody can kill), and the
punchline promotes it past every human in the building: a parking
space and a pension plan. No meeting clichés, no reply-all, just a
specific little absurdity anyone who has worked in an office
recognises on first read.

## How it runs

`main.py` is Python 3.13, standard library only, fully deterministic.
It checks the line against the gate itself (one line, 1–200
characters, not blank) and then writes it to `/output/entry.txt`
and prints it:

```sh
python3 main.py
```

## Local validation

- Output is exactly the line above: 116 characters, 116 bytes, one
  line, one sentence, inside the 1–200 gate.
- Two consecutive runs produce byte-identical output.
- `main.py` is 1,250 bytes, under the 4,096-byte per-file cap.
