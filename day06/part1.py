# Description: Day 6 Part 1 of Advent of Code
import re

def solution(textfile: str) -> int:
    """Returns the product of all number of ways to win runs"""

    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact

    times = [int(x) for x in re.findall(r'\d+', lines[0])]
    distances = [int(x) for x in re.findall(r'\d+', lines[1])]

    number_of_ways = 1
    for i in range(len(distances)):
        time = times[i]
        distance = distances[i]
        number_of_ways_race = 0
        for waiting_time in range(time):
            velocity = waiting_time
            remaining_time = time - waiting_time
            if velocity * remaining_time > distance:
                number_of_ways_race += 1
            

        number_of_ways *= number_of_ways_race

    return number_of_ways