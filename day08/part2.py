# Description: Day 8 Part 2 of Advent of Code

from math import lcm


def solution(textfile: str) -> int:
    """Returns the number of steps to reach the end on all starts"""

    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact

    nodes = {}

    instructions = lines[0].rstrip()
    tmp_instru = [0] * len(instructions)
    for instruction_index, instruction in enumerate(instructions):
        if instruction == 'R':
            tmp_instru[instruction_index] = 1

    instructions = tmp_instru

    starts = []
    
    for line in lines[2:]:
        current = line[0:3]
        next_left = line[7:10]
        next_right = line[12:15]

        if current[-1] == 'A':
            starts.append(current)


        nodes[current] = [next_left, next_right]


    counters = []
    for start in starts:
        counter = 0
        while start[-1] != 'Z':
            start = nodes[start][instructions[counter % len(instructions)]]
            counter += 1

        counters.append(counter)


    return lcm(*counters)
