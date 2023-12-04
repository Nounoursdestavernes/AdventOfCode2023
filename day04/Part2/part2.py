# Description: Day 4 Part 2 of Advent of Code 2023
import re

def part2(lines: str) -> int:
    """Returns the number of scratch cards"""
    copies = [1] * len(lines)

    for i, line in enumerate(lines):
        line = line.rstrip().split(':')[1]
        winning_numbers, picked_numbers = line.split('|')
        winning_numbers = set(re.findall(r'\d+', winning_numbers))
        picked_numbers = set(re.findall(r'\d+', picked_numbers))

        matched_number = winning_numbers.intersection(picked_numbers)
        points = len(matched_number)

        if points != 0:
            for j in range(i + 1, i + points + 1):
                copies[j] += copies[i]

    return sum(copies)
