#!/usr/bin/env python3

def execute():
    with open('2022/input/day.10.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    mem = run_program(data)
    print(render_image(mem))
    return signal_strength(mem)

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

short_input = """noop
addx 3
addx -5""".splitlines()

long_input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop
""".splitlines()

expected = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""

def run_program(program):
    x = 1
    memory = [x]
    for line in program:
        if line.startswith("addx"):
            memory.append(x)
            x += int(line[5:])
            memory.append(x)
        elif line.startswith("noop"):
            memory.append(x)
    return memory


def signal_strength(program):
    if len(program) < 220:
        return 0
    return 20 * program[20] \
        + 60 * program[60] \
        + 100 * program[100] \
        + 140 * program[140] \
        + 180 * program[180] \
        + 220 * program[220]

def render_image(program):
    if len(program) < 240:
        return ""
    raw = "".join(["#" if abs(ind%40-x) < 2 else "." for ind, x in enumerate(program[0:240])])
    return "\n".join([raw[i:i+40] for i in range(0, len(raw), 40)])

def test_cases():
    verify(run_program(short_input)[-1], -1)
    verify(run_program(long_input)[20], 21)
    verify(run_program(long_input)[60], 19)
    verify(run_program(long_input)[100], 18)
    verify(run_program(long_input)[140], 21)
    verify(run_program(long_input)[180], 16)
    verify(run_program(long_input)[220], 18)
    verify(signal_strength(run_program(long_input)), 13140)
    verify(render_image(run_program(long_input)), expected)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())