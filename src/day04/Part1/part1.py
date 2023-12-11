# Description: Day 4 Part 1 of Advent of Code 2023
import re


def part1(lines: list[str]) -> int:
    """Returns the number of points from scratch cards"""
    points = 0
    for _, line in enumerate(lines):
        line = line.rstrip().split(':')[1]
        winning_numbers, picked_numbers = line.split('|')
        winning_numbers = set(re.findall(r'\d+', winning_numbers))
        picked_numbers = set(re.findall(r'\d+', picked_numbers))

        matched_number = winning_numbers.intersection(picked_numbers)
        if len(matched_number) != 0:
            points += 2 ** (len(matched_number) - 1)

    return points