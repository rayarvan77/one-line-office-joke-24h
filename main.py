#!/usr/bin/env python3
"""One-line office joke entry.

Bounty: One-Line Office Joke: 24-Hour Sprint
(make.fun, slug u-pucuys-one-line-office-joke-24-hour-sprint-aaf86162)

The program writes a single joke line about office life to
/output/entry.txt (and prints it). The line is one sentence, well
under the 200-character gate, and needs no setup beyond itself.
"""

import os

JOKE = (
    "Our office plant has outlasted four managers and two "
    "restructures, so HR gave it a parking space and a pension plan."
)


def main() -> None:
    text = JOKE.strip()
    # Self-check against the bounty gate before writing anything:
    # the file must be UTF-8 text of 1 to 200 characters, a single
    # line, and not only white space. Fail loudly instead of
    # submitting a line the gate would refuse.
    if not (1 <= len(text) <= 200):
        raise ValueError(f"joke is {len(text)} characters, gate allows 1-200")
    if "\n" in text or not text.strip():
        raise ValueError("joke must be exactly one non-empty line")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(text)


if __name__ == "__main__":
    main()
