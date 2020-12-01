#!/usr/bin/env python3

def execute():
    with open('2020/input/1.txt') as inp:
        lines = inp.readlines()
    return multiply_to_2020([int(l.strip()) for l in lines if len(l.strip()) > 0])

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def multiply_to_2020(number_list):
    s = set()
    for n in number_list:
        if (2020-n) in s:
            return n * (2020-n)
        s.add(n)

def test_cases():
    verify(multiply_to_2020([1721,979,366,299,675,1456]), 514579)

if __name__ == "__main__":
    test_cases()
    print(execute())