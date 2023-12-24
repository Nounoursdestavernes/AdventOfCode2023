# Description: Day 24 Part 1 of Advent of Code 2023

X_MIN = 200000000000000
X_MAX = 400000000000000
Y_MIN = 200000000000000
Y_MAX = 400000000000000 

def det(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    """ Returns the determinant of two points """
    return (point1[0] * point2[1]) - (point1[1] * point2[0])

def part1(lines: list[str]) -> int:
    """ Returns the number of hailstones that will hit the test area  """
    hailstones = []
    for line in lines:
        position, celerity = line.split("@")
        x, y, z = list(map(int, position.split(",")))
        cx, cy, cz = list(map(int, celerity.split(",")))
        hailstones.append((x, y, z, cx, cy, cz))

    counter = 0
    for i in range(len(hailstones)):
        for j in range(i, len(hailstones)):
            hailstone1 = hailstones[i]
            hailstone2 = hailstones[j]
            x1, y1, _, cx1, cy1, _ = hailstone1
            h1t0 = (x1, y1) # h1t0 = hailstone1 time 0
            h1t1 = (x1 + cx1, y1 + cy1) # h1t1 = hailstone1 time 1

            x2, y2, _, cx2, cy2, _ = hailstone2
            h2t0 = (x2, y2) # h2t0 = hailstone2 time 0
            h2t1 = (x2 + cx2, y2 + cy2) # h2t1 = hailstone2 time 1


            det_lines = det((cx1, cy1), (cx2, cy2)) # det_lines = determinant of the lines
            if det_lines == 0: # if the determinant is 0, the lines are parallel
                continue

            d = (det(h1t0, h1t1), det(h2t0, h2t1)) # d = determinant of the points
            x = - (det(d, (cx1, cx2)) / det_lines) 
            y = - (det(d, (cy1, cy2)) / det_lines)

            # If the intersection point is in the past            
            if x < x1 and cx1 > 0: 
                continue
            if x > x1 and cx1 < 0:
                continue
            if y < y1 and cy1 > 0:
                continue
            if y > y1 and cy1 < 0:
                continue
            if x < x2 and cx2 > 0:
                continue
            if x > x2 and cx2 < 0:
                continue
            if y < y2 and cy2 > 0:
                continue
            if y > y2 and cy2 < 0:
                continue

            if x < X_MIN or x > X_MAX or y < Y_MIN or y > Y_MAX: # if the point is not in the test area
                continue

            counter += 1 # if the point is in the test area, increment the counter

    return counter