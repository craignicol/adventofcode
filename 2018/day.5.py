#!/usr/bin/env python3

import re
import string

def execute():
    with open('input.5.txt') as inp:
        lines = inp.readlines()
    return polymer([l.strip() for l in lines if len(l.strip()) > 0][0])

regex =  '|'.join(['(' + ''.join(a) + ')'  for a in zip(string.ascii_lowercase, string.ascii_uppercase)]) + '|' +  '|'.join(['(' + ''.join(a) + ')'  for a in zip(string.ascii_uppercase, string.ascii_lowercase)])

def polymer(pp):
    npp = re.sub(regex, '', pp)
    return len(pp) if len(pp) == len(npp) else polymer(npp)

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    verify(polymer("aA"), 0)
    verify(polymer("abBA"), 0)
    verify(polymer("abAB"), 4)
    verify(polymer("aabAAB"), 6)
    verify(polymer("dabAcCaCBAcCcaDA"), 10)

if __name__ == "__main__":
    test_cases()
    print(execute())