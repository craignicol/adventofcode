#!/usr/bin/env python3

def execute():
    with open('2015/input/12.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return sum_the_numbers(data[0]), sum_the_unred_numbers(data[0])

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

import re

def sum_the_numbers(json):
    return sum([int(i) for i in re.findall(r'-?\d+', json)])

def sum_the_unred_numbers(json):
    unred = re.sub(r'{[^{]+?:"red"[^}]*?}', '_', json)
    return sum_the_numbers(unred)

def test_cases():
    verify(sum_the_numbers('[1, 2, 3]'), 6)
    verify(sum_the_numbers('{"a":2,"b":4}'), 6)
    verify(sum_the_numbers('[[[3]]]'), 3)
    verify(sum_the_numbers('{"a":{"b":4},"c":-1}'), 3)
    verify(sum_the_numbers('{"a":[-1,1]}'), 0)
    verify(sum_the_numbers('[-1,{"a":1}]'), 0)
    verify(sum_the_numbers('[]'), 0)
    verify(sum_the_numbers(r'{}'), 0)
    verify(sum_the_unred_numbers('[1, 2, 3]'), 6)
    verify(sum_the_unred_numbers(r'[1,{"c":"red","b":2},3]'), 4)
    verify(sum_the_unred_numbers(r'{"d":"red","e":[1,2,3,4],"f":5}'), 0)
    verify(sum_the_unred_numbers('[1,"red",5]'), 6)
    verify(sum_the_unred_numbers(r'{"list":[1,"red",5]}'), 6)
    verify(sum_the_unred_numbers(r'{"list":[1,{"b":5,"d":{"c":10,"z":{},"a":"red"}},0]}'), 6)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())