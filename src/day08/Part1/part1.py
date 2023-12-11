# Description: Day 8 Part 1 of Advent of Code 2023



def part1(lines: list[str]) -> int:
    """Returns the number of steps to reach the end"""

    nodes = {}

    instructions = lines[0].rstrip()
    tmp_instru = [0] * len(instructions)
    for instruction_index, instruction in enumerate(instructions):
        if instruction == 'R':
            tmp_instru[instruction_index] = 1

    instructions = tmp_instru
    
    for line in lines[2:]:
        current = line[0:3]
        next_left = line[7:10]
        next_right = line[12:15]
    

        nodes[current] = [next_left, next_right]

    counter = 0
    start = "AAA"
    while start != "ZZZ":
        start = nodes[start][instructions[counter % len(instructions)]]
        counter += 1

    return counter
