# Description: Day 11 Part 2 of Advent of Code


EXPANSION = 999999 # we already have 1 row and 1 column of empty space, so we need to expand the grid by N-1 rows and N-1 columns

def get_distance(position1 : tuple[int, int], position2 : tuple[int, int]) -> int:
    """ Returns the distance between two points """
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])



def solution(textfile: str) -> int:
    """ Returns the sum of the distances between all pairs of points"""

    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact



    lines = [line.rstrip() for line in lines]

    reversed_lines = [""] * len(lines[0]) # we need to reverse the lines
    for j in range(len(lines[0])):
        for i in range(len(lines)):
            reversed_lines[j] += lines[i][j]

        
    lines_with_no_galaxies = []
    columns_with_no_galaxies = []

    for i, line in enumerate(lines):
        if line.count("#") == 0:
            lines_with_no_galaxies.append(i)

    for j, line in enumerate(reversed_lines):
        if line.count("#") == 0:
            columns_with_no_galaxies.append(j)

    positions = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                positions.append((i, j))

    for i, position in enumerate(positions): # we need to recalculate the positions due to the expansion
        x1, y1 = position
        counter = 0
        for el in lines_with_no_galaxies:
            if el < x1:
                counter += 1
        x1 += counter * EXPANSION
        
        counter = 0
        for el in columns_with_no_galaxies:
            if el < y1:
                counter += 1
        y1 += counter * EXPANSION
        positions[i] = (x1, y1)

    sum_distance = 0
    for i, position1 in enumerate(positions):
        for j in range(i+1, len(positions)):
            position2 = positions[j]
            sum_distance += get_distance(position1, position2)    

    return sum_distance
    

