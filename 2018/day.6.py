#!/usr/bin/env python3

from collections import defaultdict

def execute():
    with open('input.6.txt') as inp:
        lines = inp.readlines()
    return largest_area([l.strip() for l in lines if len(l.strip()) > 0])

def print_grid(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if grid[x][y] is None:
                c = '*'
            else:
                c = chr(grid[x][y])
            print(c, end='')
        print()

def grow_grid(grid):
    changes = []
    for x in range(1, len(grid)-1):
        for y in range(1, len(grid[0])-1):
            if grid[x][y] is not None:
                continue
            neighbours = [grid[x-1][y], grid[x+1][y], grid[x][y-1], grid[x][y+1]]
            neighbours = set([n for n in neighbours if n is not None])
            if len(neighbours) == 0:
                continue
            elif len(neighbours) == 1:
                changes.append((x, y, neighbours.pop())) # cache to avoid races
            else:
                changes.append((x, y, 46)) # cache to avoid races
                
    for (x, y, ident) in changes:
        grid[x][y] = ident
        
    return len(changes) > 0

def measure_area(grid):
    infinity_chars = set()
    infinity_chars.update(set(grid[1]))
    infinity_chars.update(set(grid[-2]))
    for x in grid[2:-3]:
        infinity_chars.add(x[1])
        infinity_chars.add(x[-2])
        
    # print(infinity_chars)
    
    counts = defaultdict(int)
    
    for x in range(1, len(grid)-1):
        for y in range(1, len(grid[0])-1):
            if grid[x][y] is None or grid[x][y] in infinity_chars:
                continue
            else:
                counts[grid[x][y]] += 1
    
    return counts

def largest_area(coords):
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
    grid = [[None] * (max_y+2) for i in range(max_x+2)] # + 2 so that indexing +/-1 is always success
    ident = 65
    for (x, y) in coords:
        # print(x,y,ident)
        grid[x][y] = ident
        ident += 1
    
    #print_grid(grid)
    while grow_grid(grid):
        # print_grid(grid)
        pass
    
    areas = measure_area(grid)
    
    return max(areas.values())

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
    verify(largest_area(coords.split('\n')), 17)

if __name__ == "__main__":
    test_cases()
    print(execute())