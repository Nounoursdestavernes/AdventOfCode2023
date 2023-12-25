# Description: Day 25 Part 1 of Advent of Code 2023
import random
import networkx as nx

def part1(lines: list[str]) -> int:
    """ Returns the product of the length of the partitions """
    
    graph = nx.Graph()

    for line in lines:
        line = line.rstrip()
        first_node, nodes = line.split(": ")
        nodes = nodes.split(" ")
        for node in nodes:
            graph.add_edge(first_node, node, capacity=1)

    cut_value = 0
    while cut_value != 3:
        node1 = random.choice(list(graph.nodes))
        node2 = random.choice(list(graph.nodes))
        if node1 == node2:
            continue
        cut_value, partitions = nx.minimum_cut(graph, node1, node2)

    return len(partitions[0]) * len(partitions[1])
