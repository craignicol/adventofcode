#!/usr/bin/env python3

example = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""

def execute():
    with open('2020/input/9.txt') as inp:
        lines = inp.readlines()
    xmas = [l.strip() for l in lines if len(l.strip()) > 0]
    return first_invalid([int(e) for e in xmas], 25)

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

def is_valid(preamble, next):
    for i in range(len(preamble)):
        for j in range(i+1,len(preamble)):
            if preamble[i] + preamble[j] == next:
                return True # i,j,preamble[i],preamble[j],next
    return False

def first_invalid(xmas, length):
    for i in range(len(xmas)-length):
        if not is_valid(xmas[i:i+length], xmas[i+length]):
            return xmas[i:i+length], xmas[i+length]
    return None

def find_weakness(xmas, length):
    target = first_invalid(xmas, length)
    for i in range(len(xmas)):
        total = xmas[i]
        if total >= target:
            continue
        for j in range(i+1, len(xmas)):
            total += xmas[j]
            if total > target:
                break
            if total = target:
                return xmas[i], xmas[j]
    return None

def test_cases():
    preamble = range(1,26)
    verify(is_valid(preamble, 26), True)
    verify(is_valid(preamble, 49), True)
    verify(is_valid(preamble, 100), False)
    verify(is_valid(preamble, 50), False)
    preamble = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,21,22,23,24,25,45]
    verify(is_valid(preamble, 26), True)
    verify(is_valid(preamble, 65), False)
    verify(is_valid(preamble, 64), True)
    verify(is_valid(preamble, 66), True)
    xmas = [int(e) for e in example.splitlines()]
    verify(first_invalid(xmas, 5), 127)
    verify(find_weakness(xmas, 5), 62)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())