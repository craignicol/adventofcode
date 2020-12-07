#!/usr/bin/env python3

def execute():
    with open('2015/input/3.txt') as inp:
        lines = inp.readlines()
    return houses_visited(lines[0]), houses_visited_with_robot(lines[0])

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

def route_taken(route):
    location = (0,0)
    visited = set([location])
    for step in route:
        move = movements[step]
        location = (location[0]+move[0], location[1]+move[1])
        visited.add(location)
    return visited

def houses_visited(route):
    return len(route_taken(route))

def houses_visited_with_robot(route):
    santa = route[::2]
    robot = route[1::2]
    return len(route_taken(santa).union(route_taken(robot)))

def test_cases():
    verify(houses_visited('>'), 2)
    verify(houses_visited('^>v<'), 4)
    verify(houses_visited('^v^v^v^v^v'), 2)
    verify(houses_visited_with_robot('^v'), 3)
    verify(houses_visited_with_robot('^>v<'), 3)
    verify(houses_visited_with_robot('^v^v^v^v^v'), 11)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())