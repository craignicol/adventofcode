#!/usr/bin/env python3

def execute():
    with open('input.1.txt') as inp:
        lines = [int(i) for i in inp.readlines() if len(i.strip()) != 0]
    return frequency_correct(lines)

def frequency_correct(offsets):    
    count = 0
    for o in offsets:
        count += o
        
    return count

def verify(a, b):
    if (a == b):
        return
    
    print (locals())

def test_cases():
    verify(frequency_correct([+1, -2, +3, +1]), 3)
    verify(frequency_correct([+1, +1, +1]), 3)
    verify(frequency_correct([+1, +1, -2]), 0)
    verify(frequency_correct([-1, -2, -3]), -6)

if __name__ == "__main__":
    test_cases()
    print(execute())