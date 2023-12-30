# Description: Day 18 Part 2 of Advent of Code
import re
import numpy as np 


# https://stackoverflow.com/a/30408825
# Shoelace formula
def PolyArea(x: list,y: list) -> int:
    """ x and y are arrays of polygon coordinates """
    return int(0.5 * np.abs(np.dot(x,np.roll(y,1)) - np.dot(y,np.roll(x,1))) + 0.5)


def solution(textfile: str) -> int:
    """ Return the number of cubic meters of lava that the laggoon will hold """

    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact

    current = (0, 0)
    counter = 0
    coordonates = [[], []]
    for line in lines:
        tmp = re.findall(r'(#(\d|[a-z])+)', line)[0][0]
        length = int(tmp[1:-1], base=16)
        direction = int(tmp[-1])
        match direction:
            case 0:
                direction = (0, 1)
            case 1:
                direction = (-1, 0)
            case 2:
                direction = (0, -1)
            case 3:
                direction = (1, 0)

        counter += length

        new_x = current[0] + length * direction[0]
        new_y = current[1] + length * direction[1]

        current = (new_x, new_y)
        coordonates[0].append(new_x)
        coordonates[1].append(new_y)

    # Pick's theorem
    # Area = inside_points + boundary_points / 2 - 1
    area = PolyArea(coordonates[0], coordonates[1])
    boundary_points = counter
    inside_points = area + 1 - boundary_points // 2    

    return inside_points + boundary_points