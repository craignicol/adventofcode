#!/usr/bin/env python3

example = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

def execute():
    with open('2020/input/8.txt') as inp:
        lines = inp.readlines()
    return run_until_loop_or_exit([l.strip() for l in lines if len(l.strip()) > 0])["accumulator"]

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

def run_until_loop_or_exit(code):
    accumulator = 0
    pos = 0
    seen_positions = set()
    while(pos not in seen_positions and pos < len(code)):
        seen_positions.add(pos)
        (command, value) = code[pos].split()
        if command == "nop":
            pos += 1
        elif command == "acc":
            pos += 1
            accumulator += int(value)
        elif command == "jmp":
            pos += int(value)
    return locals()

def test_cases():
    verify(run_until_loop_or_exit(example.splitlines())["accumulator"], 5)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())