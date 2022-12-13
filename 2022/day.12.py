#!/usr/bin/env python3

def execute():
    with open('2022/input/day.12.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return shortest_path(data), shortest_path(data, True)

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

sample_input = """Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".splitlines()

def shortest_path(data, multiple_start=False):
    paths = []
    visited = [[]]
    elevations = []
    target = None
    for row, line in enumerate(data):
        cell = [ord(l) - ord('a') for l in line]
        elevations.append(cell)
        paths.append([None] * len(cell))
        if "S" in line:
            start = line.index("S")
            cell[start] = 0
            paths[-1][start] = 0
            visited[-1].append((row, start))
        if multiple_start and (0 in cell):
            for start in [i for i, x in enumerate(cell) if x == 0]:
                paths[-1][start] = 0
                visited[-1].append((row, start))
        if "E" in line:
            end = line.index("E")
            cell[end] = 26
            target = (row, end)

    for s in range(1, len(paths) * len(paths[0])):
        last = visited[-1]
        visited.append([])
        for x,y in last:
            height = elevations[x][y] + 1 # Can go up at most 1
            if (x, y) == target:
                return s - 1
            if x > 0 and elevations[x - 1][y] <= height and paths[x - 1][y] is None:
                paths[x - 1][y] = s
                visited[-1].append((x - 1, y))
            if x < len(elevations) - 1 and elevations[x + 1][y] <= height and paths[x + 1][y] is None:
                paths[x + 1][y] = s
                visited[-1].append((x + 1, y))
            if y > 0 and elevations[x][y - 1] <= height and paths[x][y - 1] is None:
                paths[x][y - 1] = s
                visited[-1].append((x, y - 1))
            if y < len(elevations[x]) - 1 and elevations[x][y + 1] <= height and paths[x][y + 1] is None:
                paths[x][y + 1] = s
                visited[-1].append((x, y + 1))
    print('\n'.join(['.'.join([str(c) if c != None else '_' for c in p]) for p in paths]))
    return visited, target

def test_cases():
    verify(shortest_path(sample_input), 31)
    verify(shortest_path(sample_input, True), 29)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())