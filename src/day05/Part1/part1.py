# Description: Day 5 Part 1 of Advent of Code 2023
import re


def part1(lines: list[str]) -> int:
    """Returns the lowest location"""
    seeds = [int(x) for x in re.findall(r'\d+', lines[0])]

    mapped = [0] * len(seeds)
    for _, line in enumerate(lines[3:]):
        numbers = [int(x) for x in re.findall(r'\d+', line)]
        if numbers == []:
            mapped = [0] * len(seeds)
            continue
        for seed_index, seed in enumerate(seeds):
            if numbers[1] <= seed < numbers[1] + numbers[2] and mapped[seed_index] == 0:
                seeds[seed_index] = numbers[0] + (seed - numbers[1])    
                mapped[seed_index] = 1

    return min(seeds)