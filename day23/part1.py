# Description: Day 23 Part 1 of Advent of Code


def solution(textfile: str) -> int:
    """ Return the number of steps of the longest hike """
    
    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact
    
    
    graph = {}

    for i, line in enumerate(lines):
        for j, c in enumerate(line.strip()):
            if c == '.':
                graph[(i, j)] = []

                if i > 0:
                    top = lines[i-1][j]
                    if top != '#' and top != 'v':
                        graph[(i, j)].append((i-1, j))

                if i < len(lines) - 1:
                    bottom = lines[i+1][j]
                    if bottom != '#' and bottom != '^':
                        graph[(i, j)].append((i+1, j))

                if j > 0:
                    left = lines[i][j-1]
                    if left != '#' and left != '>':
                        graph[(i, j)].append((i, j-1))
                
                if j < len(line) - 1:
                    right = lines[i][j+1]
                    if right != '#' and right != '<':
                        graph[(i, j)].append((i, j+1))
                
            elif c == '^':
                graph[(i, j)] = []
                if i > 0:
                    top = lines[i-1][j]
                    if top != '#' and top != 'v':
                        graph[(i, j)].append((i-1, j))
            
            elif c == 'v':
                graph[(i, j)] = []
                if i < len(lines) - 1:
                    bottom = lines[i+1][j]
                    if bottom != '#' and bottom != '^':
                        graph[(i, j)].append((i+1, j))
            
            elif c == '<':
                graph[(i, j)] = []
                if j > 0:
                    left = lines[i][j-1]
                    if left != '#' and left != '>':
                        graph[(i, j)].append((i, j-1))
            
            elif c == '>':
                graph[(i, j)] = []
                if j < len(line) - 1:
                    right = lines[i][j+1]
                    if right != '#' and right != '<':
                        graph[(i, j)].append((i, j+1))

    
    start = (0, lines[0].index('.'))
    end = (len(lines) - 1, lines[-1].index('.'))

    distance = 0
    remains = [(start, [start])]

    while remains:
        current, path = remains.pop(0)

        for neighbor in graph[current]:
            if neighbor == end:
                distance = max(distance, len(path) + 1)
            elif neighbor not in path :
                remains.append((neighbor, path + [neighbor]))


    return distance - 1 # we need the number of steps