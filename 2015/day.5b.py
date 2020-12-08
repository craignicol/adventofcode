#!/usr/bin/env python3
import re

def execute():
    with open('2015/input/5.txt') as inp:
        lines = inp.readlines()
    return count_is_nice([l.strip() for l in lines if len(l.strip()) > 0])

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

def has_split_doubles(s):
    for i in range(len(s) - 2):
        if s[i] == s[i+2]:
            return True
    return False

def has_2_pairs(s):
    for i in range(len(s) - 3):
        test_pair = s[i:i+2]
        if test_pair in s[i+2:]:
            return True
    return False

def is_nice(s):
    return has_2_pairs(s) and has_split_doubles(s)

def count_is_nice(words):
    return len([w for w in words if is_nice(w)])

def test_cases():
    verify(is_nice("qjhvhtzxzqqjkmpb"), True)
    verify(is_nice("xxyxx"), True)
    verify(is_nice("uurcxstgmygtbstg"), False)
    verify(is_nice("ieodomkazucvgmuy"), False)
    verify(count_is_nice(["qjhvhtzxzqqjkmpb", "xxyxx", "uurcxstgmygtbstg", "ieodomkazucvgmuy", ""]), 2)

    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())