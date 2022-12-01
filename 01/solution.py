#!/usr/bin/env python

from collections import defaultdict
from pprint import pprint

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
    return totals

def part_1(input_data):
    totals = elf_totals(input_data)
    return max(totals)

def part_2(input_data):
    totals = elf_totals(input_data)
    return sum(sorted(totals, reverse=True)[0:3])

def main():
    with open("input.txt") as input_file:
        input_data = input_file.read()
    print(part_1(input_data))
    print(part_2(input_data))


if __name__ == "__main__":
    main()
