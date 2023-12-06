# Description: Day 6 Part 2 of Advent of Code 2023
import re


def part2(lines: list[str]) -> int:
    """Returns the number of ways to win the race"""
    tmp_time = re.findall(r'\d+', lines[0])
    time = int("".join(tmp_time))
    tmp_distance = re.findall(r'\d+', lines[1])
    distance = int("".join(tmp_distance))

    start_winning = 0
    for waiting_time in range(time):
        velocity = waiting_time
        remaining_time = time - waiting_time
        if velocity * remaining_time > distance:
            start_winning = waiting_time
            break
            
    end_winning = time + 1 - start_winning

    number_of_wins = end_winning - start_winning

    return number_of_wins

