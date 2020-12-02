#!/usr/bin/env python3
import re

def execute():
    with open('2020/input/2.txt') as inp:
        lines = inp.readlines()
    return countValidPasswords([l.strip() for l in lines if len(l.strip()) > 0])

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def isValidPassword(pattern, password):
    counts, letter = pattern.split()
    low, high = counts.split('-')
    lettercount = len(password.split(letter))-1
    return int(low) <= lettercount and lettercount <= int(high)

def countValidPasswords(password_list):
    return len([p for p in password_list if isValidPassword(*p.split(': '))])

def test_cases():
    example = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
    verify(isValidPassword("1-3 a", "abdde"), True)
    verify(isValidPassword("1-3 b", "cdefg"), False)
    verify(isValidPassword("2-9 c", "ccccccccc"), True)
    verify(countValidPasswords(example.splitlines()), 2)
    ## Answer is > 196

if __name__ == "__main__":
    test_cases()
    print(execute())