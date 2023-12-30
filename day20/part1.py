# Description: Day 20 Part 1 of Advent of Code


def solution(textfile: str) -> int:
    """ Return the product of the number of low pulses and the number of high pulses """


    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact

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


    low_power = 0
    high_power = 0
    for _ in range(1000):
        low_power += 1
        remains = [('broadcaster', 0, x) for x in broadcaster]
        while remains:
            origine, power, destination = remains.pop(0)
        
            if power:
                high_power += 1
            else:
                low_power += 1
            

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

    return high_power * low_power