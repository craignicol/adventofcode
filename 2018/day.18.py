#!/usr/bin/env python3

def execute():
    with open('input.1.txt') as inp:
        lines = inp.readlines()
    return len([l.strip() for l in lines if len(l.strip()) > 0])

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    pass

if __name__ == "__main__":
    test_cases()
    print(execute())