#!/usr/bin/env python3

def execute():
    with open('2020/input/1.txt') as inp:
        lines = inp.readlines()
    return len([l.strip() for l in lines if len(l.strip()) > 0])

tests_failed = 0
tests_executed = 0

def verify(a, b):
    tests_executed = 1
    if (a == b):
        print("✓")
        return
    
    tests_failed += 1
    print (locals())

def test_cases():
    pass

if __name__ == "__main__":
    test_cases()
    print("Failed " + tests_failed + " out of " + tests_executed + " tests. ")
    print(execute())