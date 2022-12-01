#!/usr/bin/env python3

def execute():
    with open('./input/day.1.txt') as inp:
        lines = inp.readlines()
    data = "".join(lines)
    return total_per_elf(data), most_calories(data)

tests_failed = 0
tests_executed = 0

elves_food = """
1000
2000
3000

4000

5000
6000

7000
8000
9000

10000 
"""

def verify(a, b):
    global tests_executed
    global tests_failed

    tests_executed += 1
    if (a == b):
        print("✓")
        return
    
    tests_failed += 1
    print (locals())

def total_per_elf(elves_food):
    return [sum([int(x) for x in elf.split()]) for elf in elves_food.split("\n\n")]

def most_calories(elves_food):
    return max(total_per_elf(elves_food))

def test_cases():
    verify(total_per_elf(elves_food), [6000, 4000, 11000, 24000, 10000])
    verify(most_calories(elves_food), 24000)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())