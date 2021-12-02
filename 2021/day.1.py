#!/usr/bin/env python3

def execute():
    with open('./input/day.1.txt') as inp:
        lines = inp.readlines()
    return count_increasing([l.strip() for l in lines if len(l.strip()) > 0])

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

example1 = [
199,
200,
208,
210,
200,
207,
240,
269,
260,
263
]

def count_increasing(list_num):
    list_num = [int(n) for n in list_num]
    last_num = -1
    increasing_count = -1 # First is always bigger

    for i in list_num:
        if i > last_num:
            increasing_count += 1
        last_num = i

    return increasing_count

def test_cases():
    verify(count_increasing(example1), 7)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())