# Description: Day 6 Part 2 of Advent of Code
import re

def solution(textfile: str) -> int:
    """Returns the number of ways to win the race"""

    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact

    tmp_time = re.findall(r'\d+', lines[0])
    time = int("".join(tmp_time))
    tmp_distance = re.findall(r'\d+', lines[1])
    distance = int("".join(tmp_distance))

    start_winning = 0
    end = time
    while start_winning != end:
        middle = (start_winning + end) // 2
        velocity = middle
        remaining_time = time - middle
        if velocity * remaining_time > distance:
            end = middle
        else:
            start_winning = middle + 1
            
    end_winning = time + 1 - start_winning

    number_of_wins = end_winning - start_winning

    return number_of_wins

