#!/usr/bin/env python3

def execute():
    with open('2023/input/day.1.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return calibration_result(data), parse_calibration_result(data)

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

sample_input = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""

sample_input2 = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen"""

def decode_calibration(calibration):
    numbers = [c for c in calibration if c>='0' and c<='9']
    return int(numbers[0] + numbers[-1])

def parse_decode_calibration(calibration):
    numbers = ["?", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] # Only single digit
    parsed = []
    for c in range(len(calibration)):
        for i, n in enumerate(numbers):
            if calibration[c:].startswith(n) or calibration[c] == str(i):
                parsed.append(i)
    return (parsed[0] * 10) + parsed[-1] 

def calibration_result(input):
    return sum(decode_calibration(l) for l in input)

def parse_calibration_result(input):
    return sum(parse_decode_calibration(l) for l in input)

def test_cases():
    samples = sample_input.splitlines()
    verify(decode_calibration(samples[0]), 12)
    verify(decode_calibration(samples[1]), 38)
    verify(decode_calibration(samples[2]), 15)
    verify(decode_calibration(samples[3]), 77)
    verify(calibration_result(samples), 142)
    samples2 = sample_input2.splitlines()
    verify(parse_decode_calibration(samples2[0]), 29)
    verify(parse_decode_calibration(samples2[1]), 83)
    verify(parse_decode_calibration(samples2[2]), 13)
    verify(parse_decode_calibration(samples2[3]), 24)
    verify(parse_decode_calibration(samples2[4]), 42)
    verify(parse_decode_calibration(samples2[5]), 14)
    verify(parse_decode_calibration(samples2[6]), 76)
    #29, 83, 13, 24, 42, 14, and 76.
    verify(parse_calibration_result(samples2), 281)
    print("Passed {} out of {} tests. ".format(tests_executed - tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())