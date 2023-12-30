# Description: Day 15 Part 1 of Advent of Code


def h(s:str) -> int:
    """ Hash function """
    h_value = 0
    for char in s:
        h_value += ord(char)
        h_value *= 17
        h_value %= 256
    
    return h_value


def solution(textfile: str) -> int:
    """ Returns sum of hash values of all instructions """

    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact

    instructions = lines[0].split(',')
    res = 0
    for instruction in instructions:
        res += h(instruction)
    return res