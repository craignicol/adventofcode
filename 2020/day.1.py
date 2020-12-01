#!/usr/bin/env python3

def execute():
    with open('2020/input/1.txt') as inp:
        lines = inp.readlines()
    numbers = [int(l.strip()) for l in lines if len(l.strip()) > 0]
    return multiply_to_2020(numbers), multiply_3_to_2020(numbers)

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

def multiply_3_to_2020(number_list):
    s = set()
    for n in number_list:
        for x in s:
            if (2020-n-x) in s:
                return n * x * (2020-n-x)
        s.add(n)

def test_cases():
    verify(multiply_to_2020([1721,979,366,299,675,1456]), 514579)
    verify(multiply_3_to_2020([1721,979,366,299,675,1456]), 241861950)

if __name__ == "__main__":
    test_cases()
    print(execute())