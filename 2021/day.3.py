#!/usr/bin/env python3

from statistics import mode

def execute():
    with open('./input/day.3.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return power_consumption(data), life_support_rating(data)

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
    exploded = [s < length / 2 for s in parts]
    return convert_to_int(exploded)

def gamma_rate(parts, length):
    exploded = [s > length // 2 for s in parts]
    return convert_to_int(exploded)

def power_consumption(diagnostics):
    sp = sum_parts(diagnostics)
    return epsilon_rate(sp, len(diagnostics)) * gamma_rate(sp, len(diagnostics))

def match_bit_criteria(bitcount, diagnostics, default):
    bits = powers[-bitcount:]
    while len(diagnostics) > 1:
        f = bits.pop(0)
        bit_matches = [d&f for d in diagnostics]
        if (bit_matches.count(0) == len(bit_matches)/2):
            criteria = f
        else:
            criteria = mode(bit_matches)
        if (default == 1) :
            diagnostics = [d for d in diagnostics if d&f == criteria&f]
        else:
            diagnostics = [d for d in diagnostics if d&f != criteria&f]
    return diagnostics[0]

def oxygen_generator_rating(parts, diagnostics):
    return match_bit_criteria(len(parts), diagnostics, 1)

def co2_scrubber_rating(parts, diagnostics):
    return match_bit_criteria(len(parts), diagnostics, 0)

def life_support_rating(diagnostics):
    sp = sum_parts(diagnostics)
    values = [int(d, 2) for d in diagnostics]
    return oxygen_generator_rating(sp, values) * co2_scrubber_rating(sp, values)

def test_cases():
    verify(sum_parts(example1), [7,5,8,7,5])
    verify(gamma_rate(sum_parts(example1), len(example1)), 0b10110)
    verify(epsilon_rate(sum_parts(example1), len(example1)), 0b01001)
    verify(power_consumption(example1), 198)
    verify(oxygen_generator_rating(sum_parts(example1), [int(d,2) for d in example1]), 0b10111)
    verify(co2_scrubber_rating(sum_parts(example1), [int(d,2) for d in example1]), 0b01010)
    verify(life_support_rating(example1), 230)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())