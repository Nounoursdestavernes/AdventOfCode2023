# Description: Day 1 Part 1 of Advent of Code
import string

def solution(textfile: str) -> int:
    """Returns the sum of all calibrations in the file"""

    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact

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