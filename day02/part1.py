# Description: Day 2 Part 1 of Advent of Code


def solution(textfile: str) -> int:
    """Returns the sum of the ids of the line that have possible sets"""

    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact

    sum_of_ids = 0
    conditions = {'red' : 12, 'green' : 13, 'blue': 14}

    for index_of_line, line in enumerate(lines):
        id = index_of_line + 1
        line = line.rstrip().split(':')[1].split(';') # Remove the id and split the line into sets
        possible = True
        for _, set_cubes in enumerate(line):
            dices = set_cubes[1:].split(' ') # Remove the first ' ' and split the set into dices

            for i in range(0, len(dices), 2): # Iterate over the dices dice[i] is the number and dice[i+1] is the color
                if dices[i+1][-1] == ',': # Remove the ',' from the color if it exists
                    dices[i+1] = dices[i+1][:-1]

                if int(dices[i]) > conditions[dices[i+1]]: # Check if the dice is bigger than the condition
                    possible = False
                    break # Break the loop if the dice is bigger than the condition
            if not possible:
                break 
        if possible:
            sum_of_ids += id
                  
    return sum_of_ids