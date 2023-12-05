# Description: Day 5 Part 2 of Advent of Code 2023
import re
import copy
import time

def part2(lines: list[str]) -> int:
    """Returns the lowest location"""
    input = "".join(lines)
    par = input.split("\n\n")

    initial_seeds = [int(x) for x in re.findall(r'\d+', par[0])]
    seeds = []
    for i in range(0, len(initial_seeds), 2):
        seeds.append([initial_seeds[i], initial_seeds[i] + initial_seeds[i+1] - 1])

    conv_parts = []
    for part in par[1:]:
        conv_dict = {}
        for line in part.split("\n"):
            if len(re.findall(r':', line)) != 0:
                continue
            numbers = [int(x) for x in re.findall(r'\d+', line)]

            conv_dict[numbers[1], numbers[1] + numbers[2] - 1] = numbers[0]
        conv_parts.append(conv_dict)


    for i in range(len(conv_parts)):
        d = conv_parts[i]
        interss = []
        still = copy.deepcopy(seeds)
        while still:
            a, b = still.pop()
            added = False
            for a1, b1 in d:
                dec = d[(a1, b1)]
                if a1 <= a <= b1 and a1 <= b <= b1:
                    interss.append((dec + a - a1, dec + b - a1))
                    added = True
                elif a1 <= b <= b1:
                    interss.append((dec, dec + b - a1))
                    still.append((a, a1 - 1))
                    added = True
                elif a1 <= a <= b1:
                    interss.append((dec + a - a1, dec + b1 - a1))
                    still.append((b1 + 1, b))
                    added = True
                elif a < a1 and b > b1:
                    interss.append((dec, dec + b1 - a1))
                    still.append((a, a1 - 1))
                    still.append((b1 + 1, b))
                    added = True
            if not added:
                interss.append((a, b))

        seeds = interss

    return min(seeds)[0]
