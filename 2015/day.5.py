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

def has_3_vowels(s):
    (_, count) = re.subn("[aeiou]", "_", s)
    return count >= 3

def has_doubles(s):
    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            return True
    return False

def has_bad_pairs(s):
    bad_pairs = ["ab", "cd", "pq", "xy"]
    for bp in bad_pairs:
        if bp in s:
            return True
    return False

def is_nice(s):
    return has_3_vowels(s) and has_doubles(s) and not has_bad_pairs(s)

def count_is_nice(words):
    return len([w for w in words if is_nice(w)])

def test_cases():
    verify(is_nice("ugknbfddgicrmopn"), True)
    verify(is_nice("aaa"), True)
    verify(is_nice("jchzalrnumimnmhp"), False)
    verify(is_nice("haegwjzuvuyypxyu"), False)
    verify(is_nice("dvszwmarrgswjxmb"), False)
    verify(count_is_nice(["ugknbfddgicrmopn", "aaa", "jchzalrnumimnmhp", "haegwjzuvuyypxyu", "dvszwmarrgswjxmb"]), 2)

    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())