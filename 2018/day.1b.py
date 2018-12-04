#!/usr/bin/env python3

def execute():
    with open('input.1.txt') as inp:
        lines = [int(i) for i in inp.readlines() if len(i.strip()) != 0]
    return first_duplicate_frequency(lines)

def first_duplicate_frequency(offsets):    
    count = 0
    previous = [0]
    
    while True:
        for o in offsets:
            count += o
            if count in previous:
                return count
            else:
                previous.append(count)
        print(len(previous), count, end = '\t')
        
    return count

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    verify(first_duplicate_frequency([+1, -2, +3, +1]), 2)
    
    # +1, -1 first reaches 0 twice.
    # +3, +3, +4, -2, -4 first reaches 10 twice.
    # -6, +3, +8, +5, -6 first reaches 5 twice.
    # +7, +7, -2, -7, -4 first reaches 14 twice.

    verify(first_duplicate_frequency([+1, -1]), 0)
    verify(first_duplicate_frequency([+3, +3, +4, -2, -4]), 10)
    verify(first_duplicate_frequency([-6, +3, +8, +5, -6]), 5)
    verify(first_duplicate_frequency([+7, +7, -2, -7, -4]), 14)

if __name__ == "__main__":
    test_cases()
    print(execute())