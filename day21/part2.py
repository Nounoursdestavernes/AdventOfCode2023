# Description: Day 21 Part 2 of Advent of Code

STEPS = 26501365

def polynom(n: int, a: int, b: int, c: int) -> int:
    """ Returns the value of the polynomial a + n * (b - a) + n * (n - 1) // 2 * ((c - b) - (b - a)) """
    return a + n * (b - a) + n * (n - 1) // 2 * ((c - b) - (b - a))


def solution(textfile: str) -> int:
    """ Returns the number of garden plots of land that the elf could reach """


    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact


    garden_plots = {}
    start = 0
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '.':
                garden_plots[j + i * 1j] = False
            elif char == 'S':
                start = j + i * 1j
                garden_plots[j + i * 1j] = False

    width = len(lines[0])-1 # 131
    distances = [1, 1j, -1, -1j]

    coefs = []
    plots = set()
    plots.add(start)

    counter = 2 * width + 65 # we want to have the 3 coefficients of the polynomial
    for count in range(counter+1):
        if count % width == width // 2: # if we meet the S point
            coefs.append(len(plots))

        tmp_plots = set()
        for plot in plots:
            for distance in distances:
                new_plot = plot + distance
                if new_plot.real % width + new_plot.imag % width * 1j in garden_plots:
                    tmp_plots.add(new_plot)

        plots = tmp_plots
        
                    
    a, b, c = coefs

    return polynom(STEPS//width, a, b, c)
