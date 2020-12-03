#!/usr/bin/env python3
from functools import reduce

sample = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#""".splitlines()

slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]

def execute():
    with open('2020/input/3.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return count_trees(data), multiply_trees(data)

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def count_trees(localmap, x_step = 3, y_step = 1):
    if y_step < 1:
        return 0
    # Move 3 right, 1 down
    x, y = 0, 0
    tree_count = 0
    while (y < len(localmap)):
        if localmap[y][x] == "#":
            tree_count += 1
        x = (x + x_step) % len(localmap[0])
        y += y_step
    return tree_count

def multiply_trees(localmap):
    return reduce((lambda x, y: x * y), [count_trees(localmap, *slopes[i]) for i in range(len(slopes))])

def test_cases():
    verify(count_trees(sample), 7)
    verify(count_trees(sample, *slopes[0]), 2)
    verify(count_trees(sample, *slopes[1]), 7)
    verify(count_trees(sample, *slopes[2]), 3)
    verify(count_trees(sample, *slopes[3]), 4)
    verify(count_trees(sample, *slopes[4]), 2)
    verify(multiply_trees(sample), 336)
    

if __name__ == "__main__":
    test_cases()
    print(execute())