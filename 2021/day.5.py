#!/usr/bin/env python3

def execute():
    with open('./input/day.5.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return len(data)

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

example1 = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2"""


def count_overlaps(data):
    """Note that this currently discards diagonals"""
    overlaps = 0
    for line in data:
        line = line.split(' -> ')
        start = line[0].split(',')
        end = line[1].split(',')
        start = (int(start[0]), int(start[1]))
        end = (int(end[0]), int(end[1]))
        if start[0] == end[0] or start[1] == end[1]:
            overlaps += 1
    return overlaps

def test_cases():
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())