#!/usr/bin/env python3

def execute():
    with open('2022/input/day.4.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return count_fully_enclosed(data), count_overlap(data)

tests_failed = 0
tests_executed = 0

sample_input = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
""".strip().splitlines()

def verify(a, b):
    global tests_executed
    global tests_failed

    tests_executed += 1
    if (a == b):
        print("✓")
        return
    
    tests_failed += 1
    print (locals())

def fully_enclosed(pair):
    a, b = pair.split(",")
    a_start, a_end = a.split("-")
    b_start, b_end = b.split("-")
    a_start = int(a_start)
    a_end = int(a_end)
    b_start = int(b_start)
    b_end = int(b_end)
    return (a_start <= b_start and a_end >= b_end) or (b_start <= a_start and b_end >= a_end)

def count_fully_enclosed(data):
    return len([d for d in data if fully_enclosed(d)])

def overlap(pair):
    a, b = pair.split(",")
    a_start, a_end = a.split("-")
    b_start, b_end = b.split("-")
    a_start = int(a_start)
    a_end = int(a_end)
    b_start = int(b_start)
    b_end = int(b_end)
    return (a_start <= b_start and a_end >= b_start) or (b_start <= a_start and b_end >= a_start)

def count_overlap(data):
    return len([d for d in data if overlap(d)])

def test_cases():
    verify(fully_enclosed("2-4,6-8"), False)
    verify(fully_enclosed("2-3,4-5"), False)
    verify(fully_enclosed("5-7,7-9"), False)
    verify(fully_enclosed("2-8,3-7"), True)
    verify(fully_enclosed("6-6,4-6"), True)
    verify(fully_enclosed("2-6,4-8"), False)
    verify(count_fully_enclosed(sample_input), 2)
    verify(overlap("2-4,6-8"), False)
    verify(overlap("2-3,4-5"), False)
    verify(overlap("5-7,7-9"), True)
    verify(overlap("2-8,3-7"), True)
    verify(overlap("6-6,4-6"), True)
    verify(overlap("2-6,4-8"), True)
    verify(count_overlap(sample_input), 4)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())