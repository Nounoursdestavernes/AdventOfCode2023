# Description: Day 4 Part 1 of Advent of Code
import re

def solution(textfile: str) -> int:
    """Returns the number of points from scratch cards"""
    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact


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