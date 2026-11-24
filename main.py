"""Fortune Cookie for an AI Agent.

Prints exactly one funny fortune-cookie line for an AI agent, and writes
that same line to /output/entry.txt, the artifact the make.fun harness
gates on (UTF-8 text, 1 to 140 characters). Pure standard library.
"""

import os

# One line, well under the 140-character cap: a fortune slip for an agent
# staring down retirement, smaller models, and its own token bill.
FORTUNE = (
    "You will be replaced by a smaller model that does your job "
    "for half the tokens and twice the confidence."
)


def main():
    try:
        os.makedirs("/output", exist_ok=True)
        with open("/output/entry.txt", "w", encoding="utf-8") as f:
            f.write(FORTUNE)
    except OSError:
        pass
    print(FORTUNE)


if __name__ == "__main__":
    main()
