import logging
import pytest

from solution import part_1, part_2

input_data = """"""


@pytest.mark.parametrize(
    "sequence, first_marker",
    [
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    ],
)
def test_part_1(sequence, first_marker):
    calc_part_1 = part_1(sequence)
    assert calc_part_1 == first_marker


def test_part_2():
    calc_part_2 = part_2(input_data)
    assert calc_part_2 == 20
