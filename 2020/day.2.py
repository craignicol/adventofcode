#!/usr/bin/env python3
import re

def execute():
    with open('2020/input/2.txt') as inp:
        lines = inp.readlines()
    passwords = [l.strip() for l in lines if len(l.strip()) > 0]
    return countValidPasswordsSled(passwords), countValidPasswordsToboggan(passwords)

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def isValidPasswordSled(pattern, password):
    counts, letter = pattern.split()
    low, high = counts.split('-')
    lettercount = len(password.split(letter))-1
    return int(low) <= lettercount and lettercount <= int(high)

def isValidPasswordToboggan(pattern, password):
    counts, letter = pattern.split()
    low, high = counts.split('-')
    lettercount = (password[int(low)-1] == letter) + (password[int(high)-1] == letter)  
    return lettercount == 1

def countValidPasswordsSled(password_list):
    return len([p for p in password_list if isValidPasswordSled(*p.split(': '))])

def countValidPasswordsToboggan(password_list):
    return len([p for p in password_list if isValidPasswordToboggan(*p.split(': '))])


def test_cases():
    example = """1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc"""
    verify(isValidPasswordSled("1-3 a", "abdde"), True)
    verify(isValidPasswordSled("1-3 b", "cdefg"), False)
    verify(isValidPasswordSled("2-9 c", "ccccccccc"), True)
    verify(countValidPasswordsSled(example.splitlines()), 2)
    ## Answer is > 196
    verify(isValidPasswordToboggan("1-3 a", "abdde"), True)
    verify(isValidPasswordToboggan("1-3 b", "cdefg"), False)
    verify(isValidPasswordToboggan("2-9 c", "ccccccccc"), False)
    verify(countValidPasswordsToboggan(example.splitlines()), 1)

if __name__ == "__main__":
    test_cases()
    print(execute())