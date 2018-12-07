#!/usr/bin/env python3

import re
import string

def execute():
    with open('input.5.txt') as inp:
        lines = inp.readlines()
    return minimum_polymer([l.strip() for l in lines if len(l.strip()) > 0][0])

regex =  re.compile('|'.join(['(' + ''.join(a) + ')'  for a in zip(string.ascii_lowercase, string.ascii_uppercase)]) + '|' +  '|'.join(['(' + ''.join(a) + ')'  for a in zip(string.ascii_uppercase, string.ascii_lowercase)]))

def polymer(pp):
    last = len(pp) + 1
    while len(pp) < last:
        last = len(pp)
        pp = regex.sub('', pp)
    return last

def minimum_polymer(pp):
    minimum = len(pp)
    for (l, u) in zip(string.ascii_lowercase, string.ascii_uppercase):
        stripped = pp.replace(l, '').replace(u, '')
        if len(stripped) < len(pp):
            print(l, u)
            npp = polymer(stripped)
            if npp < minimum:
                minimum = npp
    return minimum

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    verify(minimum_polymer("dabAcCaCBAcCcaDA"), 4)

if __name__ == "__main__":
    test_cases()
    print(execute())