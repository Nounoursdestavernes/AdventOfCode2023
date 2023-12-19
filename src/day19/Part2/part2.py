# Description: Day 19 Part 2 of Advent of Code 2023


def part2(lines: list[str]) -> int:
    """ Return the distinct combinations of ratings that will be accepted by the Elves' workflows  """

    workflows, items = "".join(lines).split("\n\n")

    workflows = workflows.split("\n")
    dict_workflows = {}
    for workflow in workflows:
        name, checks = workflow.split("{")
        checks = checks[:-1].split(",")
        
        tmp = []
        for check in checks:
            tmp.append(check.split(":"))
        dict_workflows[name] = tmp

    
    possibilities = []
    possibilities.append(["in", {'x':(1, 4000), 'm':(1, 4000), 'a':(1, 4000), 's':(1, 4000)}])

    accepted = []
    while possibilities:
        name, dico = possibilities.pop()
        if name == "R":
            continue
        if name == "A":
            accepted.append(dico)
            continue
        
        workflow = dict_workflows[name]

        for check in workflow:
            if len(check) == 1:
                possibilities.append([check[0], dico])
                break

            criteria = check[0][0]
            op = check[0][1]
            value = int(check[0][2:])
            min_val, max_val = dico[criteria]
         
            if min_val == max_val == value:
                continue

            if op == "<":
                if max_val < value:
                    possibilities.append([check[1], dico])
                elif value <= min_val:
                    continue
                else:
                    new_doc = dico.copy()
                    new_doc[criteria] = (min_val, value - 1)
                    possibilities.append([check[1], new_doc])
                    dico[criteria] = (value, max_val)
            elif op == ">":
                if min_val > value:
                    possibilities.append([check[1], dico])
                elif value >= max_val:
                    continue
                else:
                    new_doc = dico.copy()
                    new_doc[criteria] = (value + 1, max_val)
                    possibilities.append([check[1], new_doc])
                    dico[criteria] = (min_val, value)


    counter = 0
    for accept in accepted:
        x, m, a, s = accept.values()
        counter += (x[1] - x[0] + 1) * (m[1] - m[0] + 1) * (a[1] - a[0] + 1) * (s[1] - s[0] + 1)

    return counter