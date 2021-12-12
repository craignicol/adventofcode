#!/usr/bin/env python3

def execute():
    with open('./input/day.11.txt') as inp:
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
    while explosions != 0:
        for j in range(len(data)):
            for i in range(len(row)):
                if i == 9:
                    explosions += 1
                    
            next_data.append(next_row)
        data = next_data
    return data

def count_flashes(data, steps):
    flashes = 0
    data = parse_data(data)
    for i in range(steps):
        data = next_step(data)
        flashes += sum([row.count(0) for row in data])
    return flashes

def parse_data(data):
    return [[int(i) for i in l] for l in data]

def test_cases():
    verify(next_step(next_step(parse_data(example1))), parse_data(example1_step2))
    verify(count_flashes(example1, 100), 1656)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())