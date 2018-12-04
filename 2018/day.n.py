#!/usr/bin/env python3

def execute():
    with open('input.1.txt') as inp:
        lines = inp.readlines()
    return len(lines)

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