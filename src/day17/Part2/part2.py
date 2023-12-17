# Description: Day 17 Part 2 of Advent of Code 2023

# The main idea of the code comes from u/4HbQ on reddit 

from heapq import heappop, heappush

MIN_STRAIGHT = 4
MAX_STRAIGHT = 10

def part2(lines):
    """ Return the least heat lost """

    grid = {
        i + j*1j: int(n) 
        for i, line in enumerate(lines)
        for j, n in enumerate(line.rstrip())
    }

    step = 0
    end = (len(lines) - 1 + 1j * (len(lines[0]) - 2))
    remains = [(0,0,0,1), (0,0,0,1j)] # heat_loss, step, position and direction
    visited = set()

    while remains:
        heat_loss, _, position, direction= heappop(remains)

        if position == end: 
            return heat_loss
        
        if (position, direction) in visited:
            continue

        visited.add((position,direction))

        for next_direction in 1j/direction, -1j/direction:

            for i in range(MIN_STRAIGHT, MAX_STRAIGHT+1):
                next_position = position + next_direction * i

                if next_position in grid:
                    next_heat_loss = sum(grid[position + next_direction * j] for j in range(1,i+1))
                    step += 1
                    heappush(remains, (heat_loss + next_heat_loss, step, next_position, next_direction))
    
    return 0 