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

def grow_lanternfish(state):
    new_state = []
    for fish in state:
        if fish == 0:
            new_state.append(6) # adults have a cycle of 6
            new_state.append(8) # newborns have a cycle of 8
        else:
            new_state.append(fish - 1)
    return new_state

def count_lanternfish(initial_state, days):
    state = [int(x) for x in initial_state.split(',')]
    for _ in range(days):
        state = grow_lanternfish(state)
    return len(state)

def test_cases():
    verify(count_lanternfish(example1, 1), 5)
    verify(count_lanternfish(example1, 18), 26)
    verify(count_lanternfish(example1, 80), 5934)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())