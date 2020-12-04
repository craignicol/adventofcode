#!/usr/bin/env python3
import re

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

invalid_passports = """eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 byr:1946

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007"""

valid_passports = """pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980
hcl:#623a2f

eyr:2029 ecl:blu cid:129 byr:1989
iyr:2014 pid:896056539 hcl:#a97842 hgt:165cm

hcl:#888785
hgt:164cm byr:2001 iyr:2015 cid:88
pid:545766238 ecl:hzl
eyr:2022

iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"""

required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
optional_fields = set(["cid"])

def execute():
    with open('2020/input/4.txt') as inp:
        lines = inp.readlines()
    return count_valid_passports(''.join(lines)), count_valid_passports(''.join(lines), only_count_fields=False)

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

def validate_byr(byr):
    return 1920 <= byr and byr <= 2002

def validate_iyr(iyr):
    return 2010 <= iyr and iyr <= 2020

def validate_eyr(eyr):
    return 2020 <= eyr and eyr <= 2030

def validate_hgt(hgt):
    if len(hgt) < 3:
        return False
    value, units = int(hgt[:-2]), hgt[-2:]
    if units == "cm":
        return 150 <= value and value <= 193
    if units == "in":
        return 59 <= value and value <= 76
    return False

def validate_hcl(hcl):
    return re.match("^#[0-9a-fA-F]{6}$", hcl) is not None

eye_colours = set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])

def validate_ecl(ecl):
    return ecl in eye_colours

def validate_pid(pid):
    return re.match("^[0-9]{9}$", pid) is not None

def validate_fields(fields):
    return (
        validate_byr(int(fields["byr"])) and
        validate_iyr(int(fields["iyr"])) and
        validate_eyr(int(fields["eyr"])) and
        validate_hgt(fields["hgt"]) and
        validate_hcl(fields["hcl"]) and
        validate_ecl(fields["ecl"]) and
        validate_pid(fields["pid"])
    )

def is_valid_passport(passport, only_count_fields = True):
    fields = dict([tuple(p.split(":")) for p in passport.split()])
    return (len(required_fields.difference(fields)) == 0) and (only_count_fields or validate_fields(fields))

def count_valid_passports(passports, only_count_fields = True):
    return sum([1 for p in passports.split("\n\n") if is_valid_passport(p, only_count_fields)])

def test_cases():
    verify(is_valid_passport(passport1), True)
    verify(is_valid_passport(passport2), False)
    verify(is_valid_passport(passport3), True)
    verify(is_valid_passport(passport4), False)
    verify(count_valid_passports(allpassports), 2)
    verify(count_valid_passports(valid_passports, only_count_fields=False), 4)
    verify(count_valid_passports(invalid_passports, only_count_fields=False), 0)

    verify(validate_byr(2002), True)
    verify(validate_byr(2003), False)

    verify(validate_hgt("60in"), True)
    verify(validate_hgt("190cm"), True)
    verify(validate_hgt("190in"), False)
    verify(validate_hgt("190"), False)

    verify(validate_hcl("#123abc"), True)
    verify(validate_hcl("#123abz"), False)
    verify(validate_hcl("123abc"), False)

    verify(validate_ecl("brn"), True)
    verify(validate_ecl("wat"), False)

    verify(validate_pid("000000001"), True)
    verify(validate_pid("0123456789"), False)

    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())