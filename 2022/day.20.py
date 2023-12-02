#!/usr/bin/env python3

def execute():
    with open('2022/input/day.1.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return len(data)

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

sample_input = """1
2
-3
3
-2
0
4"""

def decrypt(encrypted):
    initial = [int(i) for i in encrypted]
    msg = initial[:]
    for i in initial:
        
    return sum([msg[1000 % len(msg)], msg[2000 % len(msg)], msg[3000 % len(msg)]])

def test_cases():
    verify(decrypt(sample_input.splitlines()), 3)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())