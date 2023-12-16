# Description: Day 16 Part 1 of Advent of Code 2023

def part1(lines: list[str]) -> int:
    """ Returns the number of tiles that are passed by the beam """

    grid = {
        complex(i,j): char 
        for j, row in enumerate(lines)
        for i, char in enumerate(row.strip())
    }

    tiles = set()
    already_seen = set()
    remains = [(-1, 1)]
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