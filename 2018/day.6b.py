#!/usr/bin/env python3

from collections import defaultdict

def execute():
    with open('input.6.txt') as inp:
        lines = inp.readlines()
    return threshold_area([l.strip() for l in lines if len(l.strip()) > 0], 10000)

def distance(point1, point2):
    return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

def threshold_area(coords, max_distance):
    coords = [tuple([int(i) for i in s.split(', ')]) for s in coords]
    min_x = 65535
    max_x = 0
    min_y = 65535
    max_y = 0
    for (x, y) in coords:
        if x < min_x:
            min_x = x
        if x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        if y > max_y:
            max_y = y

    size = 0
    for x in range(1, max_x + 1):
        for y in range(1, max_y + 1):
            total_distance = sum([distance(c, (x,y)) for c in coords])
            if total_distance < max_distance:
                size += 1
    
    return size

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    coords = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""
    verify(threshold_area(coords.split('\n'), 32), 16)

if __name__ == "__main__":
    test_cases()
    print(execute())