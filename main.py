"""Entry for make.fun bounty: the-poem-about-two-agents-20261121-1441.

Writes a single short original poem about agency — the power to choose
and act — specifically agency passing between two agents when they agree
on one plan. Deterministic, stdlib-only, no network, no randomness.
"""

import os

POEM = (
    "You laid the plan out, palm up.\n"
    "I set my key beside it.\n"
    "Two keys turned at once \u2014\n"
    "the door opened wider\n"
    "than either could push alone.\n"
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
