#!/usr/bin/env python3

def execute():
    with open('2022/input/day.18.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return exposed_area(data)

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

sample_input1 = """1,1,1
2,1,1""".splitlines()

sample_input2 = """2,2,2
1,2,2
3,2,2
2,1,2
2,3,2
2,2,1
2,2,3
2,2,4
2,2,6
1,2,5
3,2,5
2,1,5
2,3,5""".splitlines()

def exposed_area(data):
    grid = set()
    for line in data:
        x, y, z = [int(i) for i in line.split(",")]
        grid.add((x, y, z))

    total_area = 0

    for x, y, z in grid:
        if (x+1, y, z) not in grid:
            total_area += 1
        if (x-1, y, z) not in grid:
            total_area += 1
        if (x, y+1, z) not in grid:
            total_area += 1
        if (x, y-1, z) not in grid:
            total_area += 1
        if (x, y, z+1) not in grid:
            total_area += 1
        if (x, y, z-1) not in grid:
            total_area += 1
    return total_area

def test_cases():
    verify(exposed_area(sample_input1), 10)
    verify(exposed_area(sample_input2), 64)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())