#!/usr/bin/env python3

def execute():
    with open('2015/input/10.txt') as inp:
        lines = inp.readlines()
    return len(look_and_say_n_times([l.strip() for l in lines if len(l.strip()) > 0][0], 50))

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

def look_and_say(s):
    result = ""
    last = s[0]
    count = 1
    for c in s[1:]:
        if c == last:
            count += 1
        else:
            result += str(count) + last
            last = c
            count = 1
    result += str(count) + last
    return result

def look_and_say_n_times(s, n):
    for i in range(n):
        s = look_and_say(s)
    return s

def test_cases():
    verify(look_and_say("1"), "11")
    verify(look_and_say("11"), "21")
    verify(look_and_say("21"), "1211")
    verify(look_and_say("1211"), "111221")
    verify(look_and_say("111221"), "312211")
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())