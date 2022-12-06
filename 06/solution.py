#!/usr/bin/env python
"""
Usage: solution.py [options]

Options:
  -h --help             Show this help message and exit
  -d --debug            Enable debugging prints.
"""

from collections import defaultdict, deque
import logging
from pprint import pprint

import docopt


def all_different(characters):
    all_different = True
    for index, character in enumerate(characters):
        other_characters = characters.copy()
        del other_characters[index]
        for other_character in other_characters:
            if character == other_character:
                all_different = False
    return all_different


def part_1(input_data):
    input_data = input_data.strip()
    answer = None
    for line in input_data.split("\n"):
        line = line.strip()
        analyzing = deque(maxlen=4)
        for index, character in enumerate(line):
            analyzing.append(character)
            logging.debug(f"{analyzing}")
            if len(analyzing) == 4:
                if all_different(analyzing):
                    return index + 1


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
