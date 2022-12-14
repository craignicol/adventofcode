#!/usr/bin/env python3

def execute():
    with open('2022/input/day.14.txt') as inp:
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

sample_input = """498,4 -> 498,6 -> 496,6
503,4 -> 502,4 -> 502,9 -> 494,9
""".splitlines()

sand_start = (500, 0)

def parse_walls(walls):
    global sand_start
    corners = []
    minx, maxx, miny = 500, 500, 0
    for wall in walls:
        thiswall = []
        segments = wall.split(' -> ')
        for segment in segments:
            x, y = segment.split(',')
            x = int(x)
            y = int(y)
            minx = min(minx, x)
            maxx = max(maxx, x)
            miny = max(miny, y)
            thiswall.append((x, y))
        corners.append(thiswall)
    grid = [[False] * (maxx - minx + 1) for _ in range(miny + 1)]
    for wall in corners:
        for i in range(len(wall) - 1):
            x1, y1 = wall[i]
            x2, y2 = wall[i + 1]
            if x1 == x2:
                for y in range(min(y1,y2), max(y1,y2) + 1):
                    grid[y][x1 - minx] = True
            else:
                for x in range(min(x1,x2)-minx, max(x1,x2)-minx + 1):
                    grid[y1][x] = True
    sand_start = (500 - minx, 0)
    return grid

def count_walls(walls):
    return sum(len([c for c in row if c]) for row in walls)

def print_grid(walls):
    for row in walls:
        print(''.join('#' if c else '.' for c in row))

def test_cases():
    print_grid(parse_walls(sample_input))
    verify(count_walls(parse_walls(sample_input)), 20)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())