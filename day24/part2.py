# Description: Day 24 Part 2 of Advent of Code

from sympy import Symbol, solve_poly_system

def solution(textfile: str) -> int:
    """ Returns the sum of the coordinates of the initial position """

    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact

    hailstones = []
    for line in lines:
        position, celerity = line.split("@")
        x, y, z = list(map(int, position.split(",")))
        cx, cy, cz = list(map(int, celerity.split(",")))
        hailstones.append((x, y, z, cx, cy, cz))

    x = Symbol("x")
    y = Symbol("y")
    z = Symbol("z")
    cx = Symbol("cx")
    cy = Symbol("cy")
    cz = Symbol("cz")

    equations = []
    time_system = []

    for index, hailstone in enumerate(hailstones[:3]): # secret sauce is that we only need to find how to hit the first 3 hailstones to find the answer
        x1, y1, z1, cx1, cy1, cz1 = hailstone
        t = Symbol(f"t{index}")
        time_system.append(t)
        equations.append(x + cx * t - x1 - cx1 * t)
        equations.append(y + cy * t - y1 - cy1 * t)
        equations.append(z + cz * t - z1 - cz1 * t)

    result = solve_poly_system(equations, x, y, z, cx, cy, cz, *time_system)[0]

    return sum([x for x in result[:3]])