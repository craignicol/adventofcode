#!/usr/bin/env python3

def execute():
    with open('2022/input/day.18.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return exposed_area(data), exposed_area_without_air_pockets(data)

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

def exposed_area_without_air_pockets(data):
    grid = set()
    for line in data:
        x, y, z = [int(i) for i in line.split(",")]
        grid.add((x, y, z))

    total_area = 0
    maxx = max([x for x, y, z in grid])
    maxy = max([y for x, y, z in grid])
    maxz = max([z for x, y, z in grid])

    exposed = set()

    # air pockets are regions completely surrounded by cubes
    # we can find them by removing all cubes from the grid and then
    # finding all regions that are not connected to the outside
    # (i.e. the region that contains the origin)
    for _ in range(6): # 6 sides so need to do this 6 times
        for x in range(-1, maxx+2):
            for y in range(-1, maxy+2):
                for z in range(-1, maxz+2):
                    if (x, y, z) not in grid:
                        # buffer around the space
                        if x == -1 or y == -1 or z == -1 or x == maxx+1 or y == maxy+1 or z == maxz+1:
                            exposed.add((x, y, z))
                        elif (x+1, y, z) in exposed:
                            exposed.add((x, y, z))
                        elif (x-1, y, z) in exposed:
                            exposed.add((x, y, z))
                        elif (x, y+1, z) in exposed:
                            exposed.add((x, y, z))
                        elif (x, y-1, z) in exposed:
                            exposed.add((x, y, z))
                        elif (x, y, z+1) in exposed:
                            exposed.add((x, y, z))
                        elif (x, y, z-1) in exposed:
                            exposed.add((x, y, z))

    for x, y, z in grid:
        if (x+1, y, z) in exposed:
            total_area += 1
        if (x-1, y, z) in exposed:
            total_area += 1
        if (x, y+1, z) in exposed:
            total_area += 1
        if (x, y-1, z) in exposed:
            total_area += 1
        if (x, y, z+1) in exposed:
            total_area += 1
        if (x, y, z-1) in exposed:
            total_area += 1

    return total_area

def test_cases():
    verify(exposed_area(sample_input1), 10)
    verify(exposed_area(sample_input2), 64)
    verify(exposed_area_without_air_pockets(sample_input1), 10)
    verify(exposed_area_without_air_pockets(sample_input2), 58)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())