#!/usr/bin/env python3

def execute():
    with open('2015/input/12.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return sum_the_numbers(data[0])

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

def sum_the_numbers(json):
    import re
    return sum([int(i) for i in re.findall(r'-?\d+', json)])

def test_cases():
    verify(sum_the_numbers('[1, 2, 3]'), 6)
    verify(sum_the_numbers('{"a":2,"b":4}'), 6)
    verify(sum_the_numbers('[[[3]]]'), 3)
    verify(sum_the_numbers('{"a":{"b":4},"c":-1}'), 3)
    verify(sum_the_numbers('{"a":[-1,1]}'), 0)
    verify(sum_the_numbers('[-1,{"a":1}]'), 0)
    verify(sum_the_numbers('[]'), 0)
    verify(sum_the_numbers(r'{}'), 0)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())