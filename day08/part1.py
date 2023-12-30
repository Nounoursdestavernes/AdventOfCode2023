# Description: Day 8 Part 1 of Advent of Code


def solution(textfile: str) -> int:
    """Returns the number of steps to reach the end"""

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
