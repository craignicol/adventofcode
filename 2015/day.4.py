#!/usr/bin/env python3
import hashlib
import sys

def execute():
    with open('2015/input/4.txt') as inp:
        lines = inp.readlines()
    return minimal_hash(lines[0]), minimal_hash(lines[0], "000000")

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

def minimal_hash(givenprefix, targetprefix = "00000"):
    for i in range(sys.maxsize):
        m = hashlib.md5()
        m.update((givenprefix + str(i)).encode('utf-8'))
        if m.hexdigest()[0:len(targetprefix)] == targetprefix:
            return i

def test_cases():
    verify(minimal_hash("abcdef"), 609043)
    verify(minimal_hash("pqrstuv"), 1048970)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())