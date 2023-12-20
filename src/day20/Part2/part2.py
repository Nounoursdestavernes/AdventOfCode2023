# Description: Day 20 Part 2 of Advent of Code 2023

from math import lcm

def part2(lines: list[str]) -> int:
    """ Return the number of times the button is pressed """
    broadcaster = []
    ffm = {}
    cm = {}

    for line in lines:
        name, nexts = line.rstrip().split(" -> ")
        if name == "broadcaster":
            broadcaster = nexts.split(", ")
        elif name[0] == "%":
            ffm[name[1:]] = (0, nexts.split(", "))
        elif name[0] == "&":
            cm[name[1:]] = ({}, nexts.split(", "))


    for name in ffm:
        _, nexts = ffm[name]
        for next in nexts:
            if next in cm:
                cm[next][0][name] = 0

    for name in cm:
        _, nexts = cm[name]
        for next in nexts:
            if next in cm:
                cm[next][0][name] = 0


    preced = ""
    for name in cm:
        if "rx" in cm[name][1]:
            preced = name    

    validations = len(cm[preced][0])
    
    found = {}

    index = 0
    while len(found) != validations:
        index += 1
        remains = [('broadcaster', 0, x) for x in broadcaster]
        while remains:
            origine, power, destination = remains.pop(0)
            if destination == preced and power == 1 and origine not in found:
                found[origine] = index


            if destination in ffm:
                if power == 1:
                    continue
                else:
                    next_module = ffm[destination]
                    ffm[destination] = (1 - ffm[destination][0], ffm[destination][1])
                    for next in next_module[1]:
                        remains.append((destination ,ffm[destination][0], next))


            elif destination in cm:
                origines, nexts = cm[destination]
                origines[origine] = power
                cm[destination] = (origines, nexts)
                all_high = True
                for name in origines:
                    if origines[name] == 0:
                        all_high = False
                        break

                
                next_signal = 1
                if all_high:
                    next_signal = 0
                
                for next in nexts:
                    remains.append((destination, next_signal, next)) 


    
    return lcm(*list(found.values()))