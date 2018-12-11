#!/usr/bin/env python3

from collections import defaultdict

def execute():
    with open('input.7.txt') as inp:
        lines = inp.readlines()
    return elapsed_time([l.strip() for l in lines if len(l.strip()) > 0], 5, 60)

def elapsed_time(graph, elves, processing_baseline):
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
    current_time = 0
    current_work = [None] * elves
    while len(path) < target_length:
        # print(before_graph)
        options = sorted(options)
        while len(options) > 0 and None in current_work:
            node = options.pop(0) # take from the front
            processing_time = ord(node) - 64 + processing_baseline
            try:
                free_elf = current_work.index(None)
                current_work[free_elf] = (node, processing_time)
            except:
                print("All elves busy")
                break
        next_finish = sorted([w for w in current_work if w is not None], key = lambda x: x[1])[0][1] # first item, time
        current_time += next_finish
        new_work = []
        new_path = []
        for elf in current_work:
            if elf is None:
                new_work.append(None) 
            elif elf[1] > next_finish:
                new_work.append((elf[0], elf[1] - next_finish))
            else:
                new_path.append(elf[0])
                new_work.append(None)
        current_work = new_work
        new_path = sorted(new_path)

        # print(current_work)
        for node in new_path:
            path += node
            node_options = after_graph[node]
            for successor in node_options:
                before_graph[successor].remove(node)
                if len(before_graph[successor]) == 0:
                    del before_graph[successor]
            options.extend([o for o in node_options if o not in options and o not in path and o not in before_graph])
        
    return current_time

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
    verify(elapsed_time(graph.splitlines(), 2, 0), 15)

if __name__ == "__main__":
    test_cases()
    print(execute())