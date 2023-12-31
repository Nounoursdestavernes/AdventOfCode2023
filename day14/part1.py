# Description: Day 14 Part 1 of Advent of Code


def solution(textfile: str) -> int:
    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact



    lines = [line.rstrip() for line in lines]
    reversed_lines = []
    # row becomes column and column becomes row
    for i in range(len(lines[0])):
        reversed_lines.append(''.join([line[i] for line in lines]))

    result = 0
    for column in reversed_lines:
        counter = 0
        for j, char in enumerate(column[::-1]):
            if char == '#':
                if counter == 0:
                    continue
                for k in range(counter):
                    result += j - k
               
                counter = 0
            elif char == 'O':
                counter += 1

        if counter != 0:
            for k in range(counter):
                result += len(column) - k
                
    return result