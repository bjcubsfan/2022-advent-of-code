#!/usr/bin/env python
"""
Usage: solution.py [options]

Options:
  -h --help             Show this help message and exit
  -d --debug            Enable debugging prints.
"""

from collections import defaultdict
import logging
from pprint import pprint

import docopt


def part_1(input_data):
    """Playing rock paper scissors
    Encrypted guide, first column what opponent plays:

    A - Rock
    B - Paper
    C - Scissors

    What I should play:

    X - Rock
    Y - Paper
    Z - Scissors
    """

    them_code = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
    }
    me_code = {
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors",
    }
    input_data = input_data.strip()
    answer = 0
    for line in input_data.split("\n"):
        line = line.strip()
        this_score = 0
        them, me = line.split()
        them = them_code[them]
        me = me_code[me]
        if me == "Rock":
            if them == "Rock":
                this_score = 1 + 3
            elif them == "Paper":
                this_score = 1 + 0
            elif them == "Scissors":
                this_score = 1 + 6
        elif me == "Paper":
            if them == "Rock":
                this_score = 2 + 6
            elif them == "Paper":
                this_score = 2 + 3
            elif them == "Scissors":
                this_score = 2 + 0
        elif me == "Scissors":
            if them == "Rock":
                this_score = 3 + 0
            elif them == "Paper":
                this_score = 3 + 6
            elif them == "Scissors":
                this_score = 3 + 3
        answer += this_score
        logging.debug(this_score)
    return answer


def part_2(input_data):
    input_data = input_data.strip()
    answer = None
    for line in input_data.split("\n"):
        line = line.strip()
    return answer


def main():
    with open("input.txt") as input_file:
        input_data = input_file.read()
    print(part_1(input_data))
    print(part_2(input_data))


if __name__ == "__main__":
    options = docopt.docopt(__doc__)
    if options["--debug"]:
        logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    main()
