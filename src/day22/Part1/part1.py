# Description: Day 22 Part 1 of Advent of Code 2023

def part1(lines: list[str]) -> int:
    """ Returns the number of blocks that can be destroyed """
    # Parsing
    blocks = []
    for line in lines:
        start, end = line.split('~')
        x_start, y_start, z_start = start.split(',')
        x_end, y_end, z_end = end.split(',')
        blocks.append(((int(x_start), int(y_start), int(z_start)), (int(x_end), int(y_end), int(z_end))))

    blocks.sort(key = lambda x: x[0][2]) # Sort by z_start
    grid = {} # (x, y, z) -> block
    blocks_fallen = {} # block -> set of (x, y, z)


    for i, block in enumerate(blocks):
        x_start, y_start, z_start = block[0]
        x_end, y_end, z_end = block[1]
        points = []
        
        # Add all points in the block
        for x in range(x_start, x_end + 1):
            for y in range(y_start, y_end + 1):
                for z in range(z_start, z_end + 1):
                    points.append((x, y, z))

        points.sort()

        z = min(z_start, z_end)
        while z > 1: # While the block can fall
            tmp_points = []
            for point in points:
                x_p, y_p, z_p = point
                new_point = (x_p, y_p, z_p - 1)
                if new_point in grid:
                    break
                else:
                    tmp_points.append(new_point)


            if len(tmp_points) != len(points):
                break
            else:
                points = tmp_points
                z -= 1
                
        for point in points: # Add the block to the grid
            grid[point] = i
        
        blocks_fallen[i] = points # Add the block to the blocks_fallen

    # Find the number of blocks that can be destroyed
    supports_block = {}
    supported_by_block = {}
    for i in range(len(blocks)):
        supports_block[i] = set()
        supported_by_block[i] = set()

    for block in blocks_fallen:
        points = blocks_fallen[block]
        for point in points:
            x, y, z = point
            if (x, y, z + 1) in grid and grid[(x, y, z + 1)] != block:
                supported_by_block[grid[(x, y, z+1)]].add(block)
                supports_block[block].add(grid[(x, y, z+1)])
    
    counter = 0
    for block in supports_block:
        if len(supports_block[block]) == 0:
            counter += 1
        else:
            for supported_block in supports_block[block]:
                not_only_one = True
                if len(supported_by_block[supported_block]) == 1:
                    not_only_one = False
                    break
            if not_only_one:
                counter += 1
            
    return counter