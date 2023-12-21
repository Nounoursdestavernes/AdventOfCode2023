# Description: Day 21 Part 1 of Advent of Code 2023
from functools import cache

STEPS = 64

def part1(lines: list[str]) -> int:
    """ Returns the number of garden plots of land that the elf could reach """
    start = 0
    garden_plots = {}
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '.':
                garden_plots[j + i * 1j] = False
            elif char == 'S':
                start = j + i * 1j
                garden_plots[j + i * 1j] = False
    
    directions = [1, 1j, -1, -1j]

    @cache
    def neigbours(position: complex) -> list[complex]:
        res = []
        for direction in directions:
            new_position = position + direction
            if new_position in garden_plots:
                res.append(new_position)
        return res

    positions = set()
    positions.add(start)
    for _ in range(STEPS):
        next_positions = set()
        while positions:

            position = positions.pop()

            for neighbour in neigbours(position):
                next_positions.add(neighbour)
                
        positions = next_positions
    

    return len(positions)