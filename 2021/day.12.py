#!/usr/bin/env python3

def execute():
    with open('./input/day.12.txt') as inp:
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

example1 = """start-A
start-b
A-c
A-b
b-d
A-end
b-end""".splitlines()

example2 = """dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc""".splitlines()

example3 = """fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW""".splitlines()

def parse_map(map):
    return {}

def unique_paths(map):
    return []

def count_paths(map):
    return len(unique_paths(parse_map(map)))

def test_cases():
    verify(count_paths(example1), 10)
    verify(count_paths(example2), 19)
    verify(count_paths(example3), 226)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())