# Description: Day 3 Part 1 of Advent of Code 2023
import string

def is_a_symbol(char: str) -> bool:
    """Returns True if the char is a symbol"""
    not_symbol = string.digits + '.' + '\n'
    return char not in not_symbol


def is_adjacent_to_a_symbol(lines: list[str], line_index: int, char_index: int) -> bool:
    """Returns True if the char is adjacent to a symbol"""
    length_of_line = len(lines[line_index])
    length_of_lines = len(lines)
    
    if line_index == 0:
        if char_index == 0:
            return is_a_symbol(lines[line_index][char_index+1]) or is_a_symbol(lines[line_index+1][char_index]) or is_a_symbol(lines[line_index+1][char_index+1])
        elif char_index == length_of_line - 1:
            return is_a_symbol(lines[line_index][char_index-1]) or is_a_symbol(lines[line_index+1][char_index]) or is_a_symbol(lines[line_index+1][char_index-1])
        else:
            return is_a_symbol(lines[line_index][char_index-1]) or is_a_symbol(lines[line_index][char_index+1]) or is_a_symbol(lines[line_index+1][char_index]) or is_a_symbol(lines[line_index+1][char_index-1]) or is_a_symbol(lines[line_index+1][char_index+1])
    elif line_index == length_of_lines - 1:
        if char_index == 0:
            return is_a_symbol(lines[line_index][char_index+1]) or is_a_symbol(lines[line_index-1][char_index]) or is_a_symbol(lines[line_index-1][char_index+1])
        elif char_index == length_of_line - 1:
            return is_a_symbol(lines[line_index][char_index-1]) or is_a_symbol(lines[line_index-1][char_index]) or is_a_symbol(lines[line_index-1][char_index-1])
        else:
            return is_a_symbol(lines[line_index][char_index-1]) or is_a_symbol(lines[line_index][char_index+1]) or is_a_symbol(lines[line_index-1][char_index]) or is_a_symbol(lines[line_index-1][char_index-1]) or is_a_symbol(lines[line_index-1][char_index+1])
    else:
        if char_index == 0:
            return is_a_symbol(lines[line_index][char_index+1]) or is_a_symbol(lines[line_index-1][char_index]) or is_a_symbol(lines[line_index-1][char_index+1]) or is_a_symbol(lines[line_index+1][char_index]) or is_a_symbol(lines[line_index+1][char_index+1])
        elif char_index == length_of_line - 1:
            return is_a_symbol(lines[line_index][char_index-1]) or is_a_symbol(lines[line_index-1][char_index]) or is_a_symbol(lines[line_index-1][char_index-1]) or is_a_symbol(lines[line_index+1][char_index]) or is_a_symbol(lines[line_index+1][char_index-1])
        else:
            return is_a_symbol(lines[line_index][char_index-1]) or is_a_symbol(lines[line_index][char_index+1]) or is_a_symbol(lines[line_index-1][char_index]) or is_a_symbol(lines[line_index-1][char_index-1]) or is_a_symbol(lines[line_index-1][char_index+1]) or is_a_symbol(lines[line_index+1][char_index]) or is_a_symbol(lines[line_index+1][char_index-1]) or is_a_symbol(lines[line_index+1][char_index+1])


def get_number(line: str, line_index: int, char_index: int) -> int:
    """Returns the number at the position"""
    number = ''
    number_positions = []
    char = line[char_index]
    char_index_save = char_index
    length_of_line = len(line)

    while char in string.digits:
        number += char
        number_positions.append([line_index, char_index])
        char_index -= 1
        if char_index == -1:
            break
        char = line[char_index]

    number = number[::-1]
    char_index = char_index_save + 1

    if char_index != length_of_line:
        char = line[char_index]

        while char in string.digits:
            number += char
            number_positions.append([line_index, char_index])
            char_index += 1
            if char_index == length_of_line:
                break
            char = line[char_index]

    return number, number_positions


def part1(lines: list[str]) -> int:
    """Returns the sum of the engine part"""
    sum_of_engine_part = 0

    number_position_already_used = []

    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if char in string.digits:
                if is_adjacent_to_a_symbol(lines, line_index, char_index):
                    if [line_index, char_index] in number_position_already_used:
                        continue
                    number, number_positions = get_number(line, line_index, char_index)   
                    number_position_already_used.extend(number_positions)
                    sum_of_engine_part += int(number)

    return sum_of_engine_part   
    