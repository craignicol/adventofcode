#!/usr/bin/env python3

def execute():
    with open('2015/input/3.txt') as inp:
        lines = inp.readlines()
    return houses_visited(lines[0])

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

movements = {
    "^": (0, 1),
    "v": (0, -1),
    "<": (-1, 0),
    ">": (1, 0)
}

def houses_visited(route):
    location = (0,0)
    visited = set([location])
    for step in route:
        move = movements[step]
        location = (location[0]+move[0], location[1]+move[1])
        visited.add(location)
    return len(visited)

def test_cases():
    verify(houses_visited('>'), 2)
    verify(houses_visited('^>v<'), 4)
    verify(houses_visited('^v^v^v^v^v'), 2)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())