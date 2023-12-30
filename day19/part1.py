# Description: Day 19 Part 1 of Advent of Code

import re


def solution(textfile: str) -> int:
    """ Returns the sum of all the valid categories for each part """
    
    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact
    
    
    accepted = set()
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

    items = items.split("\n")
    for i, item in enumerate(items):
        categories = re.findall(r"\d+", item)
        items[i] = list(map(int, categories))

    accepted = []
    for item in items:
        start = "in"
        x, m, a, s = item
        while start != "A" and start != "R":
            workflow = dict_workflows[start]
            for check in workflow:
                if len(check) == 1:
                    start = check[0]
                    break

                if eval(check[0], {"x": x, "m": m, "a": a, "s": s}):
                    start = check[1]
                    break
                    

        if start == "A":
            accepted.append(item) 


    return sum(sum(el) for el in accepted)