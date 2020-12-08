#!/usr/bin/env python3

program1 = "turn on 0,0 through 999,999"
program2 = "toggle 0,0 through 999,0"
program3 = "turn off 499,499 through 500,500"

def execute():
    with open('2015/input/6.txt') as inp:
        lines = inp.readlines()
    return count_lights([l.strip() for l in lines if len(l.strip()) > 0])

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

def turn(command, input_lights):
    if command == "turnon":
        return [1] * len(input_lights)
    elif command == "turnoff":
        return [0] * len(input_lights)
    else:
        return [x^1 for x in input_lights]

def count_lights(program):
    lights = [0] * 1_000_000
    for op in program:
        parsed = op.split()
        (topleft, _, bottomright) = parsed[-3:]
        command = ''.join(parsed[:-3])
        (top, left) = [int(n) for n in topleft.split(",")]
        (bottom, right) = [int(n) for n in bottomright.split(",")]
        for i in range(top, bottom+1):
            offset = i * 1000
            lights[offset+left:offset+right+1] = turn(command, lights[offset+left:offset+right+1]) 
    return sum(lights)

def test_cases():
    verify(count_lights([program1]), 1_000_000)
    verify(count_lights([program2]), 1_000)
    verify(count_lights([program3]), 0)
    verify(count_lights([program1, program2]), 999_000)
    verify(count_lights([program1, program3]), 999_996)
    verify(count_lights([program2, program3]), 1_000)
    verify(count_lights([program1, program2, program3]), 998_996)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())