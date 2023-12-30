# Description: Day 5 Part 2 of Advent of Code
import re

def solution(textfile: str) -> int:
    """Returns the lowest location"""

    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact

    initial_seeds = [int(x) for x in re.findall(r'\d+', lines[0])]
    seeds = []
    for i in range(0, len(initial_seeds), 2):
        seeds.append([initial_seeds[i], initial_seeds[i] + initial_seeds[i+1] - 1])

    tmp_seeds = []
    for _, line in enumerate(lines[3:]):
        numbers = [int(x) for x in re.findall(r'\d+', line)]

        if len(numbers) == 0 and re.findall(r':', line) == []:
            seeds.extend(tmp_seeds)
            tmp_seeds = []
            continue
        if len(numbers) == 0:
            continue

        maps = [numbers[0], numbers[1], numbers[1] + numbers[2] - 1]
    
        counter = 0
        while (counter < len(seeds)):
            seed = seeds[counter]
            if seed[0] > maps[2] or seed[1] < maps[1]:
                counter += 1
                continue
            elif maps[1] <= seed[0] and seed[1] <= maps[2]:
                tmp_interval = [seed[0], seed[1]]
                dec = maps[0] - maps[1]
                interval = [x + dec for x in tmp_interval]
                tmp_seeds.append(interval)
                seeds.pop(counter)
            elif seed[0] <= maps[1] and maps[2] <= seed[1]:
                if seed[0] == maps[1]:
                    tmp_interval_mdl = [maps[1], maps[2]]
                    interval_aft = [maps[2] + 1, seed[1]]
                    dec = maps[0] - maps[1]
                    interval_mdl = [x + dec for x in tmp_interval_mdl]
                    seeds.append(interval_aft)
                    tmp_seeds.append(interval_mdl)
                    seeds.pop(counter)
                elif seed[1] == maps[2]:
                    tmp_interval_mdl = [maps[1], maps[2]]
                    interval_pre = [seed[0], maps[1] - 1]
                    dec = maps[0] - maps[1]
                    interval_mdl = [x + dec for x in tmp_interval_mdl]
                    seeds.append(interval_pre)
                    tmp_seeds.append(interval_mdl)
                    seeds.pop(counter)
                else:
                    tmp_interval_mdl = [maps[1], maps[2]]
                    interval_pre = [seed[0], maps[1] - 1]
                    interval_aft = [maps[2] + 1, seed[1]]
                    dec = maps[0] - maps[1]
                    interval_mdl = [x + dec for x in tmp_interval_mdl]
                    seeds.append(interval_pre)
                    seeds.append(interval_aft)
                    tmp_seeds.append(interval_mdl)
                    seeds.pop(counter)
            elif seed[0] <= maps[1] <= seed[1] <= maps[2]:
                tmp_interval = [maps[1], seed[1]]
                interval_pre = [seed[0], maps[1] - 1]
                dec = maps[0] - maps[1]
                interval = [x + dec for x in tmp_interval]
                seeds.append(interval_pre)
                tmp_seeds.append(interval)
                seeds.pop(counter)
            elif maps[1] <= seed[0] <= maps[2] <= seed[1]:
                tmp_interval = [seed[0], maps[2]]
                interval_aft = [maps[2] + 1, seed[1]]
                dec = maps[0] - maps[1]
                interval = [x + dec for x in tmp_interval]
                seeds.append(interval_aft)
                tmp_seeds.append(interval)
                seeds.pop(counter)

    seeds.extend(tmp_seeds)
    return min(seeds)[0]
