#!/usr/bin/env python3

def execute():
    with open('2022/input/day.1.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return len(data)

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

def snafu_to_int(snafu):
    val = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
    mult = 1
    result = 0
    for c in reversed(snafu):
        result += val[c] * mult
        mult *= 5
    return result

def int_to_snafu(i):
    units = {0: "0", 1: "1", 2: "2", 3: "1=", 4: "1-"}
    return units[i % 5]

def test_cases():
    verify(int_to_snafu(0), "0")
    verify(int_to_snafu(10), "20")
    verify(int_to_snafu(20), "2=")
    verify(snafu_to_int("0"), 0)
    verify(snafu_to_int("2=-01"), 976)
    verify(int_to_snafu(1), "1")
    verify(int_to_snafu(2), "2")
    verify(int_to_snafu(3), "1=")
    verify(int_to_snafu(4), "1-")
    verify(int_to_snafu(5), "10")
    verify(int_to_snafu(6), "11")
    verify(int_to_snafu(7), "12")
    verify(int_to_snafu(8), "2=")
    verify(int_to_snafu(9), "2-")
    verify(int_to_snafu(10), "20")
    verify(int_to_snafu(15), "1=0")
    verify(int_to_snafu(20), "1-0")
    verify(int_to_snafu(2022), "1=11-2")
    verify(int_to_snafu(12345), "1-0---0")
    verify(int_to_snafu(314159265), "1121-1110-1=0")
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())