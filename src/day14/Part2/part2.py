# Description: Day 14 Part 2 of Advent of Code 2023

# Idea from https://github.com/mtpauly for this second part of the problem
# Mine was to stock local cycle and compute only changes but it was too slow

CYCLES = 1_000_000_000

def total_load(lines : list[list[str]]) -> int:
    """ Compute the total load of the support """
    total_load = 0
    length = len(lines)
    for _, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == 'O':
                total_load += length - j
    return total_load


def move_west(lines : list[list[str]]) -> list[list[str]]:
    """ Move the rocks to the west """
    for line in lines:
        free_place_index = 0

        for i, char in enumerate(line):
            if char == "#":
                free_place_index = i + 1
            elif char == "O":
                line[i] = "."
                line[free_place_index] = "O"
                free_place_index += 1

    return lines


def rotate_right(lines : list[list[str]]) -> list[list[str]]:
    """ Rotate the support to the left """
    return [[line[i] for line in lines[::-1]] for i in range(len(lines[0]))]

def rotate_left(lines : list[list[str]]) -> list[list[str]]:
    """ Rotate the support to the right """
    return [[line[i] for line in lines] for i in range(len(lines[0]))][::-1]


def part2(lines: list[str]) -> int:
    """ Compute the total load of the support after CYCLES cycles """

    lines = [list(line.rstrip()) for line in lines]
    height, width = len(lines), len(lines[0])
    lines = rotate_left(lines) # so north is to the left to start
    
    steps = {}
    indice_step = 0
    found_cycle = False

    while not found_cycle:
        lines_str = "".join(["".join(line) for line in lines])

        if lines_str in steps: # if we already have this step it means we found a cycle
            break

        steps[lines_str] = indice_step

        for _ in range(4): # 4 rotations to have a complete cycle
            lines = move_west(lines) # move rocks
            lines = rotate_right(lines) # rotate to the right to have next step facing the left

        indice_step += 1

    cycle_len = indice_step - steps[lines_str] 
    position_in_the_cycle = (CYCLES - steps[lines_str]) % cycle_len # position of the support at the end of CYCLES cycles
    lines_str = list(steps)[indice_step - cycle_len + position_in_the_cycle] # final configuration of the support in the str format

    final_position = []
    for i in range(height):
        final_position.append(list(lines_str[height * i : height * i + width]))

    return total_load(final_position)