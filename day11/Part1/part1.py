# Description: Day 11 Part 1 of Advent of Code 2023

def get_distance(position1 : tuple[int, int], position2 : tuple[int, int]) -> int:
    """ Returns the distance between two points """
    return abs(position1[0] - position2[0]) + abs(position1[1] - position2[1])


def part1(lines : list[str]) -> int:
    """ Returns the sum of the distances between all pairs of points"""
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
    
    # We recreate the grid with the empty spaces
    for i, el in enumerate(lines_with_no_galaxies):
        lines.insert(i+el, "." * len(lines[0]))
    
    for i in range(len(lines)):
        for j, el in enumerate(columns_with_no_galaxies):
            lines[i] = lines[i][:el+1+j] + "." + lines[i][j+1+el:]


    # We get the positions of the galaxies
    positions = []
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "#":
                positions.append((i, j))

    sum_distance = 0
    for i, position1 in enumerate(positions):
        for j in range(i+1, len(positions)):
            position2 = positions[j]
            sum_distance += get_distance(position1, position2)        

    return sum_distance
    

