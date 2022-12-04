#!/usr/bin/env python3

def execute():
    with open('2015/input/9.txt') as inp:
        lines = inp.readlines()
    return shortest_distance(create_graph([l.strip() for l in lines if len(l.strip()) > 0]))

tests_failed = 0
tests_executed = 0

distances = """London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141""".splitlines()

def verify(a, b):
    global tests_executed
    global tests_failed

    tests_executed += 1
    if (a == b):
        print("✓")
        return
    
    tests_failed += 1
    print (locals())

def create_graph(distances):
    graph = {}
    for line in distances:
        parts = line.split()
        if parts[0] not in graph:
            graph[parts[0]] = {}
        if parts[2] not in graph:
            graph[parts[2]] = {}
        graph[parts[0]][parts[2]] = int(parts[4])
        graph[parts[2]][parts[0]] = int(parts[4])
    return graph

def shortest_route_from(graph, current, distance, visited):
    if len(visited) == len(graph):
        yield distance
    else:
        for next in graph[current]:
            if next not in visited:
                yield from shortest_route_from(graph, next, distance + graph[current][next], visited | {next})

def shortest_route(graph, start):
    return min(shortest_route_from(graph, start, 0, set([start])))

def shortest_distance(graph):
    return min(shortest_route(graph, start) for start in graph)

def test_cases():
    verify(create_graph(distances), {'London': {'Dublin': 464, 'Belfast': 518}, 'Dublin': {'London': 464, 'Belfast': 141}, 'Belfast': {'London': 518, 'Dublin': 141}})
    verify(shortest_distance(create_graph(distances)), 605)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())