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
        conv_dict = conv_parts[i]
        tmp_seeds = []
        still = seeds
        while still:
            seed_start, seed_end = still.pop()
            added = False
            for map_start, map_end in conv_dict:
                dec = conv_dict[(map_start, map_end)]
                if map_start <= seed_start <= map_end and map_start <= seed_end <= map_end:
                    tmp_seeds.append((dec + seed_start - map_start, dec + seed_end - map_start))
                    added = True
                elif map_start <= seed_end <= map_end:
                    tmp_seeds.append((dec, dec + seed_end - map_start))
                    still.append((seed_start, map_start - 1))
                    added = True
                elif map_start <= seed_start <= map_end:
                    tmp_seeds.append((dec + seed_start - map_start, dec + map_end - map_start))
                    still.append((map_end + 1, seed_end))
                    added = True
                elif seed_start < map_start and seed_end > map_end:
                    tmp_seeds.append((dec, dec + map_end - map_start))
                    still.append((seed_start, map_start - 1))
                    still.append((map_end + 1, seed_end))
                    added = True
            if not added:
                tmp_seeds.append((seed_start, seed_end))

        seeds = tmp_seeds

    return min(seeds)[0]
