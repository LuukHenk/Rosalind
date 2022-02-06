#!/usr/bin/env python3

import os
import re

PRACTICE = False

#------

if PRACTICE:
    PRACTICE_INP = """
        10
        1 2
        4 10
        2 8
        5 9
        6 10
        7 9
    """

PATH = os.path.abspath(__file__)
INP_DIR = '{}/input'.format(os.path.dirname(PATH))

def load_input_file(INP_FILE = ''):
    if INP_FILE == '' and os.path.exists(INP_DIR):
        INP_FILE = '{}/rosalind_{}.txt'.format(INP_DIR, os.path.splitext(os.path.basename(PATH))[0])

    try:
        with open(INP_FILE, 'r') as myfile:
            INP = myfile.read()

        print('Opened \"{}\" ...\n-------\n'.format(INP_FILE))

    except IOError:
        print('Unable to locate the input file {}'.format(INP_FILE))
        exit()

    return INP

def main():
    # Load and filter input
    inp = PRACTICE_INP if PRACTICE else load_input_file()
    inp = list(filter(None, inp.split("\n")))
    inp = [list(filter(None, x.split(" "))) for x in inp]
    inp = list(filter(None, inp))
    inp = [list(map(int, x)) for x in inp]

    total_nodes = inp.pop(0)[0]
    inp.sort()

    # Build the graph using the given edges
    graph = [inp[0]]
    for edge in inp[1:]:

        # Check if an node already exists in the graph
        i = 0
        graph_len = len(graph)
        while i < graph_len:

            # If one of the nodes is already in the graph, add them to their network
            if edge[0] in graph[i] or edge[1] in graph[i]:
                graph[i].append(edge[0])
                graph[i].append(edge[1])
                graph[i] = list(set(graph[i]))
                break

            # If there is an new edge, add it to the graph
            if i == graph_len - 1:
                graph.append(edge)

            i += 1

    # Create a list of all possible nodes and check if they are all in the graph
    nodes = list(range(1, total_nodes+1))
    for edge in graph:
        for node in edge:
            if node in nodes:
                nodes.remove(node)

    # If there is a node left, add it to the graph
    for node in nodes:
        graph.append([node])

    #count how many edges there are missing for building a tree
    print(len(graph) - 1)

#------

if __name__ == "__main__":
    main()
