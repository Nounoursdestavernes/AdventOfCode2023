# Description: Day 23 Part 2 of Advent of Code 2023

def part2(lines: list[str]) -> int:
    """ Return the number of steps of the longest hike """
    graph = {}

    for i, line in enumerate(lines):
        for j, c in enumerate(line.strip()):
            if c != '#':
                graph[j + i * 1j] = {}
        
    for position in graph:
        for direction in [1, -1, 1j, -1j]:
            new_position = position + direction
            if new_position in graph:
                graph[position][new_position] = 1

    for position in graph:
        if len(graph[position]) == 2:
            neighbor1, neighbor2 = graph[position].keys()

            graph[neighbor1].pop(position)
            graph[neighbor2].pop(position)

            graph[neighbor1][neighbor2] = sum(graph[position].values())
            graph[neighbor2][neighbor1] = sum(graph[position].values())


    start = (lines[0].index('.'))
    end = (lines[-1].index('.') + (len(lines) - 1) * 1j)

    ans = 0
    remains = [(start, 0, [start])]

    while remains:
        position, distance, path = remains.pop()
        if position == end:
            ans = max(ans, distance)
        for neighbor in graph[position]:
            if neighbor not in path:
                remains.append((neighbor, distance + graph[position][neighbor] , path + [neighbor]))
    return ans