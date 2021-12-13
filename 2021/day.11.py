#!/usr/bin/env python3

def execute():
    with open('./input/day.11.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return count_flashes(data, 100)

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

example1 = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526""".splitlines()

example1_step1 = """6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637""".splitlines()

example1_step2 = """8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848""".splitlines()


def next_step(data):
    data = [[i + 1 for i in row] for row in data]
    explosions = None
    flashes = 0
    while explosions != 0:
        explosions = 0
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] is not None and data[i][j] > 9:
                    explosions += 1
                    data[i][j] = None # None here to avoid duplicate flashes
                    for x in range(-1,2): # i.e. [-1,2)
                        for y in range(-1,2):
                            if i+x in range(len(data)) and j+y in range(len(data[i])) and data[i+x][j+y] is not None:
                                data[i+x][j+y] += 1
        flashes += explosions
    data = [[i if i is not None else 0 for i in row] for row in data] # Convert None back to 0
    return data, flashes

def count_flashes(data, steps):
    flashes = 0
    data = parse_data(data)
    for _ in range(steps):
        data, next_flashes = next_step(data)
        flashes += next_flashes
    return flashes

def parse_data(data):
    return [[int(i) for i in l] for l in data]

def test_cases():
    verify(next_step(parse_data(example1))[0], parse_data(example1_step1))
    verify(next_step(parse_data(example1_step1))[0], parse_data(example1_step2))
    verify(count_flashes(example1, 100), 1656)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())