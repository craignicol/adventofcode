#!/usr/bin/env python3

def execute():
    with open('./input/day.7.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return least_fuel(data[0]), least_fuel(data[0], calculate_fuel_triangle)

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

example1 = """16,1,2,0,4,2,7,1,2,14"""

def triangle(n):
    return n*(n+1)//2

def calculate_fuel_triangle(x, positions):
    return sum([triangle(abs(x-p)) for p in positions])

def calculate_fuel(x, positions):
    return sum([abs(x-p) for p in positions])

def least_fuel(current_positions, fuel_fn=calculate_fuel):
    positions = [int(x) for x in current_positions.split(',')]
    fuel_costs = []
    for x in range(min(positions), max(positions)):
        fuel_costs.append(fuel_fn(x, positions))
    return min(fuel_costs)

def test_cases():
    verify(least_fuel(example1, calculate_fuel), 37)
    verify(least_fuel(example1, calculate_fuel_triangle), 168)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())