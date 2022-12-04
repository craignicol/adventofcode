#!/usr/bin/env python3

def execute():
    with open('./input/day.3.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return total_priority(data)

tests_failed = 0
tests_executed = 0
sample_input = """
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
""".strip().splitlines()

def verify(a, b):
    global tests_executed
    global tests_failed

    tests_executed += 1
    if (a == b):
        print("✓")
        return
    
    tests_failed += 1
    print (locals())

def common_item(s):
    comp1, comp2 = set(s[:len(s)//2]), set(s[len(s)//2:])
    return comp1.intersection(comp2).pop()

def priority(c):
    return ord(c) - ord('a') + 1 if ord(c) >= ord('a') else ord(c) - ord('A') + 27

def total_priority(data):
    return sum([priority(common_item(s)) for s in data])

def test_cases():
    verify(common_item(sample_input[0]), "p")
    verify(common_item(sample_input[1]), "L")
    verify(common_item(sample_input[2]), "P")
    verify(common_item(sample_input[3]), "v")
    verify(common_item(sample_input[4]), "t")
    verify(common_item(sample_input[5]), "s")
    verify(priority("p"), 16)
    verify(priority("L"), 38)
    verify(priority("P"), 42)
    verify(priority("v"), 22)
    verify(priority("t"), 20)
    verify(priority("s"), 19)
    verify(total_priority(sample_input), 157)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())