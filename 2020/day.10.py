#!/usr/bin/env python3

example1 = """16
10
15
5
1
11
7
19
6
12
4"""

example2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

def execute():
    with open('2020/input/10.txt') as inp:
        lines = inp.readlines()
    return count_jolts([l.strip() for l in lines if len(l.strip()) > 0])

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

def count_jolts(adapters):
    adapters = [0] + [int(a) for a in adapters]
    adapters.sort()
    count_1s, count_3s = 0, 0
    for i in range(len(adapters)):
        if i == len(adapters) - 1:
            count_3s += 1
        else:
            diff = adapters[i+1] - adapters[i]
            if diff == 1:
                count_1s += 1
            elif diff == 3:
                count_3s += 1
    return (count_1s, count_3s, count_1s*count_3s)

def test_cases():
    verify(count_jolts(example1.splitlines()), (7, 5, 35))
    verify(count_jolts(example2.splitlines()), (22, 10, 220))
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())