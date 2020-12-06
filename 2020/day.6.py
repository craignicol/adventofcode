#!/usr/bin/env python3

group1 = """abcx
abcy
abcz"""

group2 = """abc

a
b
c

ab
ac

a
a
a
a

b"""

group3 = """abc

a
b
c

ab
ac

a
a
a
a

b"""

def execute():
    with open('2020/input/6.txt') as inp:
        lines = inp.readlines()
    declaration = ''.join(lines)
    return yes_any_group_count(declaration), yes_all_group_count(declaration)

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

def any_group_count(answers):
    any_yes = set()
    for person in answers.split():
        any_yes.update(person[:])
    return len(any_yes)

def yes_any_group_count(allanswers):
    return sum([any_group_count(a) for a in allanswers.split("\n\n")])

def all_group_count(answers):
    all_yes = set("abcdefghijklmnopqrstuvwxyz"[:])
    for person in answers.split():
        all_yes.intersection_update(person[:])
    return len(all_yes)

def yes_all_group_count(allanswers):
    return sum([all_group_count(a) for a in allanswers.split("\n\n")])

def test_cases():
    verify(any_group_count(group1), 6)
    verify(yes_any_group_count(group2), 11)
    verify(yes_all_group_count(group3), 6)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())