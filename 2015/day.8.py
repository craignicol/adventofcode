#!/usr/bin/env python3
import re

def execute():
    with open('2015/input/8.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return length_diff(data), length_diff([expanded(i) for i in data])

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

sample_input = r"""
""
"abc"
"aaa\"aaa"
"\x27"
""".strip().splitlines()

def lengths(input):
    stripped = re.sub(r"(\\\")|(\\\\)|(\\x[0-9a-f]{2})", "X", input[1:-1])
    return (len(input), len(stripped))

def length_diff(input):
    return sum([l[0] - l[1] for l in [lengths(i) for i in input]])

def expanded(input):
    return '"' + input.replace("\\", "\\\\").replace('"', '\\"') + '"'

def test_cases():
    verify(lengths(sample_input[0]), (2, 0))
    verify(lengths(sample_input[1]), (5, 3))
    verify(lengths(sample_input[2]), (10, 7))
    verify(lengths(sample_input[3]), (6, 1))
    verify(length_diff(sample_input), 12)
    verify(expanded(sample_input[0]), r'"\"\""')
    verify(expanded(sample_input[1]), r'"\"abc\""')
    verify(expanded(sample_input[2]), r'"\"aaa\\\"aaa\""')
    verify(expanded(sample_input[3]), r'"\"\\x27\""')
    verify(length_diff([expanded(i) for i in sample_input]), 19)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())