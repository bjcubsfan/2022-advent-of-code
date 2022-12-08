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
import string

import docopt


def part_1(input_data):
    input_data = input_data.strip()
    total = 0
    for line in input_data.split("\n"):
        line = line.strip()
        middle = int(len(line) / 2)
        first_half, second_half = line[0:middle],  line[middle:]
        first_half = set(first_half)
        second_half = set(second_half)
        in_both = first_half & second_half
        assert len(in_both) == 1
        total += string.ascii_letters.index(in_both.pop()) + 1
    return total


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
