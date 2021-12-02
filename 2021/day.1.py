#!/usr/bin/env python3

def execute():
    with open('./input/day.1.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return count_increasing(data), count_increasing(data, 3)

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

def count_increasing(list_num, window_size = 1):
    list_num = [int(n) for n in list_num]
    last_num = [-1] * window_size
    last_sum = sum(last_num)
    increasing_count = -window_size # First is always bigger

    for i in list_num:
        last_num = last_num[1:] + [i]
        if sum(last_num) > last_sum:
            increasing_count += 1
        last_sum = sum(last_num)

    return increasing_count

def test_cases():
    verify(count_increasing(example1), 7)
    verify(count_increasing(example1, 3), 5)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())