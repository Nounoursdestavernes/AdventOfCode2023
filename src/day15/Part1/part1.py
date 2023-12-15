# Description: Day 15 Part 1 of Advent of Code 2023

def h(s:str) -> int:
    """ Hash function """
    h_value = 0
    for char in s:
        h_value += ord(char)
        h_value *= 17
        h_value %= 256
    
    return h_value


def part1(lines: list[str]) -> int:
    """ Returns sum of hash values of all instructions """
    instructions = lines[0].split(',')
    res = 0
    for instruction in instructions:
        res += h(instruction)
    return res