# Description: Day 6 Part 2 of Advent of Code 2023
import re


def part2(lines: list[str]) -> int:
    """Returns the number of ways to win the race"""
    tmp_time = re.findall(r'\d+', lines[0])
    time = int("".join(tmp_time))
    tmp_distance = re.findall(r'\d+', lines[1])
    distance = int("".join(tmp_distance))

    number_of_ways_race = 0
    for waiting_time in range(time):
        velocity = waiting_time
        remaining_time = time - waiting_time
        if velocity * remaining_time > distance:
            number_of_ways_race += 1
    
    return number_of_ways_race

