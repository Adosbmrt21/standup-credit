"""Writes one one-liner about AI coding agents to /output/entry.txt.

The joke, aimed at make.fun's comedy judge (surprise, truth, economy,
freshness): the agent does the whole job; the human keeps the credit.

    The AI writes my code, reviews my code, and answers my tickets -
    my only remaining job is taking credit in standup.

The program is deterministic: it writes the same bytes on every run,
which the competition's two-runs-identical rule requires.
"""
import os

# One joke, fixed bytes: the judge reads exactly this text and nothing else.

JOKE = ("The AI writes my code, reviews my code, and answers my tickets \u2014 "
        "my only remaining job is taking credit in standup.")


def main():
    out_dir = os.environ.get('MAKEFUN_OUTPUT_DIR', '/output')
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, 'entry.txt'), 'w', encoding='utf-8') as fh:
        fh.write(JOKE)


if __name__ == '__main__':
    main()
