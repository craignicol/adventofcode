#!/usr/bin/env python3

passport1 = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm"""

passport2 = """iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929"""

passport3 = """hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm"""

passport4 = """hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

allpassports = """ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
byr:1937 iyr:2017 cid:147 hgt:183cm

iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
hcl:#cfa07d byr:1929

hcl:#ae17e1 iyr:2013
eyr:2024
ecl:brn pid:760753108 byr:1931
hgt:179cm

hcl:#cfa07d eyr:2025 pid:166559648
iyr:2011 ecl:brn hgt:59in"""

required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
optional_fields = set(["cid"])

def execute():
    with open('2020/input/4.txt') as inp:
        lines = inp.readlines()
    return count_valid_passports(''.join(lines))

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

def is_valid_passport(passport):
    fields = dict([tuple(p.split(":")) for p in passport.split()])
    return len(required_fields.difference(fields)) == 0 

def count_valid_passports(passports):
    return sum([1 for p in passports.split("\n\n") if is_valid_passport(p)])

def test_cases():
    verify(is_valid_passport(passport1), True)
    verify(is_valid_passport(passport2), False)
    verify(is_valid_passport(passport3), True)
    verify(is_valid_passport(passport4), False)
    verify(count_valid_passports(allpassports), 2)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())