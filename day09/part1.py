# Description: Day 9 Part 1 of Advent of Code

import re

def decompose(numbers: list[int]) -> int:
    """ Decompose a list of numbers into a list of differences between each number and the next one. """
    numbers_tmp = numbers.copy()
    lasts_sum = 0
    while numbers_tmp.count(0) != len(numbers_tmp):
        tmp = []
        for i in range(len(numbers_tmp)-1):
            tmp.append(numbers_tmp[i+1] - numbers_tmp[i])

        numbers_tmp = tmp
        lasts_sum += numbers_tmp[-1]

    return lasts_sum

def solution(textfile: str) -> int:
    """ Return the sum of the predictions at the end of each line."""

    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact
    global_predictions = 0
    for line in lines:
        numbers = [int(x) for x in re.findall(r'-?\d+', line)]
        lasts_sum = decompose(numbers)

        global_predictions += lasts_sum + numbers[-1]
            
    return global_predictions
