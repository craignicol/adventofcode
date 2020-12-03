#!/usr/bin/env python3

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
.#..#...#.#"""

def execute():
    with open('2020/input/3.txt') as inp:
        lines = inp.readlines()
    return count_trees([l.strip() for l in lines if len(l.strip()) > 0])

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def count_trees(localmap):
    # Move 3 right, 1 down
    x, y = 0, 0
    tree_count = 0
    while (y < len(localmap)):
        if localmap[y][x] == "#":
            tree_count += 1
        x = (x + 3) % len(localmap[0])
        y += 1
    return tree_count

def test_cases():
    verify(count_trees(sample.splitlines()), 7)

if __name__ == "__main__":
    test_cases()
    print(execute())