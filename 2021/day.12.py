#!/usr/bin/env python3

from typing import DefaultDict


def execute():
    with open('./input/day.12.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return count_paths(data)

tests_failed = 0
tests_executed = 0

def verify(a, b):
    global tests_executed
    global tests_failed

    tests_executed += 1
    if (a == b):
        print("✓")
        return
    
    tests_failed += 1
    print (locals())

example1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".splitlines()

example2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""".splitlines()

example3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""".splitlines()

def parse_map(map):
    result = DefaultDict(set)
    for route in map:
        source, dest = route.split('-')
        result[source].add(dest)
        result[dest].add(source)
    return result

def unique_paths(map):
    visited = set()
    unvisited = set()
    all = set(map.keys())
    unvisited.add('start')
    paths = [['start']]
    l = 0
    while len([p for p in paths if p[-1] != 'end']) > 0: # We're still growing
        l = len(paths)
        current = unvisited.pop()
        visited.add(current)
        if current == 'end':
            continue
        for dest in map[current]:
            unvisited.add(dest)
            for p in paths[:]:
                if p[-1] == current:
                    if dest.isupper() or dest not in p: 
                        paths.append(p + [dest])
        paths = [p for p in paths if p[-1] != current] # remove dead ends
    return [p for p in paths if p[-1] == 'end']

def count_paths(map):
    p = unique_paths(parse_map(map))
    return len(p) # if len(p) > 20 else p

def test_cases():
    verify(count_paths(example1), 10)
    verify(count_paths(example2), 19)
    verify(count_paths(example3), 226)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())