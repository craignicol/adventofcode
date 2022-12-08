#!/usr/bin/env python3

def execute():
    with open('2015/input/11.txt') as inp:
        lines = inp.readlines()
    return next_password([l.strip() for l in lines if len(l.strip()) > 0][0])

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

def two_separate_pairs(password): 
    pairs = []
    found_pairs = set()
    for i in range(len(password)-1):
        if password[i] == password[i+1] and i not in found_pairs:
            pairs.append(password[i])
            found_pairs.add(i)
    return len(set(pairs)) > 1

def next_password(password):
    password = list(password)
    while True:
        for i in range(len(password)-1, -1, -1):
            if password[i] == 'z':
                password[i] = 'a'
            else:
                password[i] = chr(ord(password[i]) + 1)
                break
        if not any(c in password for c in 'iol'):
            if any(password[i] == chr(ord(password[i+1]) - 1) and password[i+1] == chr(ord(password[i+2]) - 1) for i in range(len(password)-2)):
                if two_separate_pairs(password):
                    if len(set(password)) < len(password):
                        return ''.join(password)

def test_cases():
    verify(next_password("abcdefgh"), "abcdffaa")
    verify(next_password("ghijklmn"), "ghjaabcc")
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())