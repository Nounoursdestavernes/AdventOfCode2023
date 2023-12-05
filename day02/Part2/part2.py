# Description: Day 2 Part 2 of Advent of Code 2023

def part2(lines: list[str]) -> int:
    """Returns the sum of the line's power"""
    sum_of_power = 0

    for _, line in enumerate(lines):
        power = 1
        line = line.rstrip().split(':')[1].split(';') # Remove the id and split the line into sets
        fewer_dices = {'red': 0, 'green': 0, 'blue': 0}
        for _, set_cubes in enumerate(line):
            dices = set_cubes[1:].split(' ') # Remove the first ' ' and split the set into dices

            for i in range(0, len(dices), 2): # Iterate over the dices dice[i] is the number and dice[i+1] is the color
                if dices[i+1][-1] == ',': # Remove the ',' from the color if it exists
                    dices[i+1] = dices[i+1][:-1]

                dice_value = int(dices[i])
                fewer_dice_value = fewer_dices[dices[i+1]]

                if dice_value > fewer_dice_value: 
                    fewer_dices[dices[i+1]] = dice_value

        for _, value in fewer_dices.items():
            power *= value

        sum_of_power += power
            
    return sum_of_power