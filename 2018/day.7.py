#!/usr/bin/env python3

from collections import defaultdict

def execute():
    with open('input.7.txt') as inp:
        lines = inp.readlines()
    return traverse([l.strip() for l in lines if len(l.strip()) > 0])

def traverse(graph):
    # construct
    after_graph = defaultdict(list)
    before_graph = defaultdict(list)
    root = None
    for edge in graph:
        from_vertex = edge[5]
        to_vertex = edge[36]
        if root is None:
            root = from_vertex
        after_graph[from_vertex].append(to_vertex)
        before_graph[to_vertex].append(from_vertex)
    
    # traverse
    path = ''
    options = [root]
    target_length = len(after_graph) + 1
    while len(path) < target_length:
        # print(before_graph)
        options = sorted(options)
        node = options.pop(0) # take from the front
        path += node
        node_options = after_graph[node]
        for successor in node_options:
            before_graph[successor].remove(node)
            if len(before_graph[successor]) == 0:
                del before_graph[successor]
        options.extend([o for o in node_options if o not in options and o not in path and o not in before_graph])
        
    return path

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    graph = """Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin."""
    verify(traverse(graph.splitlines()), "CABDFE")

if __name__ == "__main__":
    test_cases()
    print(execute())