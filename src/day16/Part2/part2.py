# Description: Day 16 Part 2 of Advent of Code 2023

def calculate_beam(grid: dict[complex, str], start: tuple[complex, complex]) -> int:
    """ Returns the number of tiles that are passed by the beam """
    tiles = set()
    already_seen = set()
    remains = [start]
    while remains:
        position, direction = remains.pop()

        if (position, direction) in already_seen:
            continue

        already_seen.add((position, direction))
        tiles.add(position)
        new_position = position + direction

        match grid.get(new_position):
            case '.':
                remains.append((new_position, direction))
            case '-':
                if direction.imag == 0:
                    remains.append((new_position, direction))
                else:
                    remains.append((new_position, 1))
                    remains.append((new_position, -1))
            case '|': 
                if direction.real == 0:
                    remains.append((new_position, direction))
                else:
                    remains.append((new_position, 1j))
                    remains.append((new_position, -1j))
            case '/':
                remains.append((new_position, -direction.imag - direction.real * 1j))
            case '\\':
                remains.append((new_position, direction.imag + direction.real * 1j))        
            case None:
                continue

    return len(tiles)-1 # remove the starting point because it is out of bounds




def part2(lines: list[str]) -> int:
    """ Returns the maximum number of tiles that are passed by the beam """
    max_tiles = 0

    grid = {
        complex(i,j): char 
        for j, row in enumerate(lines)
        for i, char in enumerate(row.strip())
    }

    height = len(lines)
    width = len(lines[0]) - 1

    for index in range(width):
        position = index -1j
        nb_tiles = calculate_beam(grid, (position, 1j))
        if nb_tiles > max_tiles:
            max_tiles = nb_tiles
        
        position = index + height * 1j
        nb_tiles = calculate_beam(grid, (position, -1j))
        if nb_tiles > max_tiles:
            max_tiles = nb_tiles

    for index in range(height):
        position = -1 + index * 1j
        nb_tiles = calculate_beam(grid, (position, 1))
        if nb_tiles > max_tiles:
            max_tiles = nb_tiles
        
        position = width + index * 1j
        nb_tiles = calculate_beam(grid, (position, -1))
        if nb_tiles > max_tiles:
            max_tiles = nb_tiles
    

    return max_tiles