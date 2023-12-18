# Description: Day 18 Part 1 of Advent of Code 2023
import re

def part1(lines: list[str]) -> int:
    """ Return the number of cubic meters of lava that the laggoon will hold """

    start = (0, 0)
    current = start
    visited = set()
    visited.add(current)
    cycle = False
    for line in lines:
        direction = line[0]
        length = re.findall(r'\d+', line)[0]
        for _ in range(int(length)):
            if direction == 'R':
                current = (current[0], current[1] + 1)
            elif direction == 'L':
                current = (current[0], current[1] - 1)
            elif direction == 'U':
                current = (current[0] - 1, current[1])
            elif direction == 'D':
                current = (current[0] + 1, current[1])

            if current == start:
                cycle = True
                break

            visited.add(current)
        if cycle:
            break
    
    min_height = min(visited, key=lambda x: x[0])[0]
    min_width = min(visited, key=lambda x: x[1])[1]

    visited = list(visited)
    visited = [(x[0] + abs(min_height) + 1, x[1] + abs(min_width) + 1) for x in visited] # to make sure we have positive numbers and we hade a line and a column to the grid at the beginning

    height = max(visited, key=lambda x: x[0])[0]
    width = max(visited, key=lambda x: x[1])[1]

    remains = [(0,0)]
    seen = set()
    while remains:
        x, y = remains.pop()
        seen.add((x, y))
        furture_positions = []
        if x + 1 <= height + 1:
            furture_positions.append((x + 1, y))
        if x - 1 >= 0:
            furture_positions.append((x - 1, y))
        if y + 1 <= width + 1:
            furture_positions.append((x, y + 1))
        if y - 1 >= 0:
            furture_positions.append((x, y - 1))

        for pos in furture_positions:
            if pos not in seen and pos not in remains and pos not in visited:
                remains.append(pos)


    counter = (width+2) * (height+2) - len(seen)


    return counter