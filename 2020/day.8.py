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
    code = [l.strip() for l in lines if len(l.strip()) > 0]
    return run_until_loop_or_exit(code)["accumulator"], flip_until_halt(code)

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

uncorrupt = {
    "jmp": "nop",
    "nop": "jmp",
    "acc": "acc"
}

def run_until_loop_or_exit(code, flip=None):
    # For Part 2, flip n-th instruction
    accumulator = 0
    pos = 0
    seen_positions = set()
    possibly_corrupt = 0
    while(pos not in seen_positions and pos < len(code)):
        seen_positions.add(pos)
        (command, value) = code[pos].split()
        if possibly_corrupt == flip:
            command = uncorrupt[command]
        if command == "nop":
            pos += 1
            possibly_corrupt += 1
        elif command == "acc":
            pos += 1
            accumulator += int(value)
        elif command == "jmp":
            pos += int(value)
            possibly_corrupt += 1
    halting = pos not in seen_positions
    return locals()

def flip_until_halt(code):
    for i in range(len(code)):
        result = run_until_loop_or_exit(code, i)
        if result["halting"]:
            return result["accumulator"]
    return None

def test_cases():
    verify(run_until_loop_or_exit(example.splitlines())["accumulator"], 5)
    verify(flip_until_halt(example.splitlines()), 8)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())