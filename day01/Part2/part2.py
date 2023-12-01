# Description: Day 1 Part 2 of Advent of Code 2023
import string

also_digits = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]


def part2(filename : str) -> int:
    """Returns the sum of all calibrations in the file"""

    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    sum_of_calibrations = 0

    for _, line in enumerate(lines):
        first_digit = 0
        last_digit = 0
        for j, char in enumerate(line):

            if char in string.digits:
                if first_digit == 0:
                    first_digit = char
                last_digit = char
                
            for k in range(3, 6):
                if line[j:j+k] in also_digits:
                    real_digit = also_digits.index(line[j:j+k]) + 1
                    if first_digit == 0:
                        first_digit = real_digit
                    last_digit = real_digit
                    j += k
                    break


        sum_of_calibrations += 10 * int(first_digit) + int(last_digit)

    return sum_of_calibrations
