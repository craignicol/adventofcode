#!/usr/bin/env python3

from typing import DefaultDict


def execute():
    with open('./input/day.12.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return count_paths(data), count_paths_with_reuse(data)

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

def clone_key(map, key):
    result = DefaultDict(set)
    result[key] = map[key].copy()
    result["0"] = map[key].copy()
    for k in map.keys():
        if k != key:
            result[k] = map[k].copy()
            if key in map[k]:
                result[k].add("0")
    return result

def unclone_paths(paths, key):
    result = []
    for p in paths:
        result.append(",".join(p).replace("0", key))
    return result

def unique_paths_with_reuse(map):
    paths = set()
    for source in map.keys():
        if source.islower() and source not in ['0', 'start', 'end']:
            reuse_paths = unique_paths(clone_key(map, source))
            paths.update(set(unclone_paths(reuse_paths, source)))
    return paths

def count_paths(map):
    p = unique_paths(parse_map(map))
    return len(p) # if len(p) > 20 else p

def count_paths_with_reuse(map):
    p = unique_paths_with_reuse(parse_map(map))
    return len(p) # if len(p) > 20 else p

def test_cases():
    verify(count_paths(example1), 10)
    verify(count_paths(example2), 19)
    verify(count_paths(example3), 226)
    verify(count_paths_with_reuse(example1), 36)
    verify(count_paths_with_reuse(example2), 103)
    verify(count_paths_with_reuse(example3), 3509)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())