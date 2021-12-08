#!/usr/bin/env python3

def execute():
    with open('./input/day.6.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return len(data), count_lanternfish(data[0], 80)

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

example1 = """3,4,3,1,2"""

# 5 5 6 7 9 10 10 10 10 11 12 15 17 19 20 20 21 22 26

def count_lanternfish(initial_state, days):
    state = [int(x) for x in initial_state.split(',')]
    count = len(state)
    for i in range(days):
        count += state.count(i % 6) + state.count((i-2) % 6)
    return count

def test_cases():
    verify(count_lanternfish(example1, 0), 5)
    verify(count_lanternfish(example1, 1), 5)
    verify(count_lanternfish(example1, 2), 6)
    verify(count_lanternfish(example1, 3), 7)
    verify(count_lanternfish(example1, 4), 9)
    verify(count_lanternfish(example1, 5), 10)
    verify(count_lanternfish(example1, 6), 10)
    verify(count_lanternfish(example1, 7), 10)
    verify(count_lanternfish(example1, 8), 10)
    verify(count_lanternfish(example1, 9), 11)
    verify(count_lanternfish(example1, 10), 12)
    verify(count_lanternfish(example1, 11), 15)
    verify(count_lanternfish(example1, 12), 17)
    verify(count_lanternfish(example1, 13), 19)
    verify(count_lanternfish(example1, 14), 10)
    verify(count_lanternfish(example1, 15), 20)
    verify(count_lanternfish(example1, 16), 21)
    verify(count_lanternfish(example1, 17), 22)
    verify(count_lanternfish(example1, 18), 26)
    verify(count_lanternfish(example1, 80), 5934)
    verify(count_lanternfish(example1, 256), 26984457539)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())