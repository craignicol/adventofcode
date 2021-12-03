#!/usr/bin/env python3

def execute():
    with open('./input/day.3.txt') as inp:
        lines = inp.readlines()
    return power_consumption([l.strip() for l in lines if len(l.strip()) > 0])

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

example1= """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split('\n')

def sum_parts(diagnostics):
    exploded = [s[:] for s in diagnostics]
    accumulator = [0] * len(exploded[0])
    for next in exploded:
        for i, v in enumerate(next):
            accumulator[i] += int(v)
    return accumulator

powers = [8192, 4096, 2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]

def convert_to_int(exploded):
    return sum([a for (a,b) in zip(powers[-len(exploded):], exploded) if b])

def epsilon_rate(parts, length):
    exploded = [s > length // 2 for s in parts]
    return convert_to_int(exploded)

def gamma_rate(parts, length):
    exploded = [s < length / 2 for s in parts]
    return convert_to_int(exploded)

def power_consumption(diagnostics):
    sp = sum_parts(diagnostics)
    return epsilon_rate(sp, len(diagnostics)) * gamma_rate(sp, len(diagnostics))

def test_cases():
    verify(sum_parts(example1), [7,5,8,7,5])
    verify(epsilon_rate(sum_parts(example1), len(example1)), 0b10110)
    verify(gamma_rate(sum_parts(example1), len(example1)), 0b01001)
    verify(power_consumption(example1), 198)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())