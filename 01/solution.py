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


def elf_totals(input_data):
    input_data = input_data.strip()
    totals = []
    curr_elf = 0
    for line in input_data.split("\n"):
        line = line.strip()
        if line == "":
            totals.append(curr_elf)
            curr_elf = 0
        else:
            curr_elf += int(line)
    # Do not forget the last elf
    totals.append(curr_elf)
    logging.debug(totals)
    return totals


def part_1(input_data):
    totals = elf_totals(input_data)
    return max(totals)


def part_2(input_data):
    totals = elf_totals(input_data)
    logging.debug(sorted(totals, reverse=True)[0:3])
    return sum(sorted(totals, reverse=True)[0:3])


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
