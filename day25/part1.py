# Description: Day 25 Part 1 of Advent of Code
import random
import networkx as nx

def solution(textfile: str) -> int:
    """ Returns the product of the length of the partitions """

    # Artifact due to change of the template
    lines = textfile.splitlines()
    lines = [line+"\n" for line in lines]
    lines[-1] = lines[-1][:-1]

    # End of artifact

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
