# Description: Day 3 Part 2 of Advent of Code
import string

def is_adjacent_to_digits(lines: list[str], line_index: int, char_index: int) -> list:
    """Returns a list of positions of the adjacent digits"""
    length_of_line = len(lines[line_index])
    length_of_lines = len(lines)
    digits_positions = []

    if line_index == 0:
        if char_index == 0:
            if lines[line_index][char_index+1] in string.digits:
                digits_positions.append([line_index, char_index+1])
            if lines[line_index+1][char_index] in string.digits:
                digits_positions.append([line_index+1, char_index])
            if lines[line_index+1][char_index+1] in string.digits:
                digits_positions.append([line_index+1, char_index+1])
        elif char_index == length_of_line - 1:
            if lines[line_index][char_index-1] in string.digits:
                digits_positions.append([line_index, char_index-1])
            if lines[line_index+1][char_index] in string.digits:
                digits_positions.append([line_index+1, char_index])
            if lines[line_index+1][char_index-1] in string.digits:
                digits_positions.append([line_index+1, char_index-1])
        else:
            if lines[line_index][char_index-1] in string.digits:
                digits_positions.append([line_index, char_index-1])
            if lines[line_index][char_index+1] in string.digits:
                digits_positions.append([line_index, char_index+1])
            if lines[line_index+1][char_index] in string.digits:
                digits_positions.append([line_index+1, char_index])
            if lines[line_index+1][char_index-1] in string.digits:
                digits_positions.append([line_index+1, char_index-1])
            if lines[line_index+1][char_index+1] in string.digits:
                digits_positions.append([line_index+1, char_index+1])
    elif line_index == length_of_lines - 1:
        if char_index == 0:
            if lines[line_index][char_index+1] in string.digits:
                digits_positions.append([line_index, char_index+1])
            if lines[line_index-1][char_index] in string.digits:
                digits_positions.append([line_index-1, char_index])
            if lines[line_index-1][char_index+1] in string.digits:
                digits_positions.append([line_index-1, char_index+1])
        elif char_index == length_of_line - 1:
            if lines[line_index][char_index-1] in string.digits:
                digits_positions.append([line_index, char_index-1])
            if lines[line_index-1][char_index] in string.digits:
                digits_positions.append([line_index-1, char_index])
            if lines[line_index-1][char_index-1] in string.digits:
                digits_positions.append([line_index-1, char_index-1])
        else:
            if lines[line_index][char_index-1] in string.digits:
                digits_positions.append([line_index, char_index-1])
            if lines[line_index][char_index+1] in string.digits:
                digits_positions.append([line_index, char_index+1])
            if lines[line_index-1][char_index] in string.digits:
                digits_positions.append([line_index-1, char_index])
            if lines[line_index-1][char_index-1] in string.digits:
                digits_positions.append([line_index-1, char_index-1])
            if lines[line_index-1][char_index+1] in string.digits:
                digits_positions.append([line_index-1, char_index+1])
    else:
        if char_index == 0:
            if lines[line_index][char_index+1] in string.digits:
                digits_positions.append([line_index, char_index+1])
            if lines[line_index-1][char_index] in string.digits:
                digits_positions.append([line_index-1, char_index])
            if lines[line_index-1][char_index+1] in string.digits:
                digits_positions.append([line_index-1, char_index+1])
            if lines[line_index+1][char_index] in string.digits:
                digits_positions.append([line_index+1, char_index])
            if lines[line_index+1][char_index+1] in string.digits:
                digits_positions.append([line_index+1, char_index+1])
        elif char_index == length_of_line - 1:
            if lines[line_index][char_index-1] in string.digits:
                digits_positions.append([line_index, char_index-1])
            if lines[line_index-1][char_index] in string.digits:
                digits_positions.append([line_index-1, char_index])
            if lines[line_index-1][char_index-1] in string.digits:
                digits_positions.append([line_index-1, char_index-1])
            if lines[line_index+1][char_index] in string.digits:
                digits_positions.append([line_index+1, char_index])
            if lines[line_index+1][char_index-1] in string.digits:
                digits_positions.append([line_index+1, char_index-1])
        else:
            if lines[line_index][char_index-1] in string.digits:
                digits_positions.append([line_index, char_index-1])
            if lines[line_index][char_index+1] in string.digits:
                digits_positions.append([line_index, char_index+1])
            if lines[line_index-1][char_index] in string.digits:
                digits_positions.append([line_index-1, char_index])
            if lines[line_index-1][char_index-1] in string.digits:
                digits_positions.append([line_index-1, char_index-1])
            if lines[line_index-1][char_index+1] in string.digits:
                digits_positions.append([line_index-1, char_index+1])
            if lines[line_index+1][char_index] in string.digits:
                digits_positions.append([line_index+1, char_index])
            if lines[line_index+1][char_index-1] in string.digits:
                digits_positions.append([line_index+1, char_index-1])
            if lines[line_index+1][char_index+1] in string.digits:
                digits_positions.append([line_index+1, char_index+1])
            
    return digits_positions
    

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



def solution(textfile: str) -> int:
    """Returns the sum of the line's engine part"""

    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact

    sum_of_engine_part = 0

    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if char == "*":
                digits_positions = is_adjacent_to_digits(lines, line_index, char_index)
                if len(digits_positions) == 0:
                    continue

                numbers = []
                position_already_used = []

                for digit_position in digits_positions:
                    number, number_positions = get_number(lines[digit_position[0]], digit_position[0], digit_position[1])
                    already_used = False

                    for position in number_positions:
                        if position in position_already_used:
                            already_used = True
                            break

                    if already_used:
                        continue

                    numbers.append(int(number))
                    position_already_used.extend(number_positions)
                
                if len(numbers) == 2:
                    sum_of_engine_part += numbers[0] * numbers[1]
                
    return sum_of_engine_part   
