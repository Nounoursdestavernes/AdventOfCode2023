# Description: Day 1 Part 1 of Advent of Code 2023
import string


def part1(lines: list[str]) -> int:
    """Returns the sum of all calibrations in the file"""
    sum_of_calibrations = 0

    for _, line in enumerate(lines):
        first_digit = 0
        last_digit = 0     
        for _, char in enumerate(line):
            if char in string.digits:
                if first_digit == 0:
                    first_digit = char
                last_digit = char

        sum_of_calibrations += 10 * int(first_digit) + int(last_digit)

    return sum_of_calibrations
