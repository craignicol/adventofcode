#!/usr/bin/env python3

from collections import defaultdict

def execute():
    with open('./input/day.5.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return count_overlaps(data, ignore_diag=True), count_overlaps(data, ignore_diag=False)

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
5,5 -> 8,2""".splitlines()

def get_range(start, end):
    x_dir = 1 if end[0] >= start[0] else -1
    y_dir = 1 if end[1] >= start[1] else -1
    x_range = range(start[0], end[0] + x_dir, x_dir) if start[0] != end[0] else [start[0]] * (abs(end[1] - start[1]) + 1)
    y_range = range(start[1], end[1] + y_dir, y_dir) if start[1] != end[1] else [start[1]] * (abs(end[0] - start[0]) + 1)
    return [(x,y) for (x,y) in zip(x_range, y_range)]

def count_overlaps(data, ignore_diag):
    """Note that this currently discards diagonals"""
    vents_sparse = defaultdict(int)
    for line in data:
        line = line.split(' -> ')
        start = line[0].split(',')
        end = line[1].split(',')
        start = (int(start[0]), int(start[1]))
        end = (int(end[0]), int(end[1]))
        if start[0] == end[0] or start[1] == end[1] or not ignore_diag: # Horizontal or vertical
            for x,y in get_range(start, end):
                vents_sparse[(x,y)] += 1
    return len([v for v in vents_sparse.values() if v > 1])

def test_cases():
    verify(count_overlaps(example1, ignore_diag=True), 5)
    verify(count_overlaps(example1, ignore_diag=False), 12)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())