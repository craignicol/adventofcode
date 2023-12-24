#!/usr/bin/env python3

from functools import reduce
from itertools import accumulate
import operator


def execute():
    with open('2023/input/day.6.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return margin_of_error(data), wins([l.replace(' ', '') for l in data])

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

sample_input = """Time:      7  15   30
Distance:  9  40  200"""

def possible_distance(time):
    result = []
    for i in range(time):
        result.append((time - i) * i) # speed * time
    return result

def possible_wins(records):
    times = [int(x) for x in records[0].split(':')[1].split()]
    distances = [int(x) for x in records[1].split(':')[1].split()]
    return [(possible_distance(t),d) for t,d in zip(times, distances)]

def wins(records):
    return [len([d for d in distance if d > record]) for distance,record in possible_wins(records)]

def margin_of_error(records):
    return reduce(operator.mul, wins(records), 1)

def test_cases():
    verify(wins(sample_input.splitlines()), [4, 8, 9])
    verify(margin_of_error(sample_input.splitlines()), 288)
    verify(wins(sample_input.replace(' ', '').splitlines())[0], 71503)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())