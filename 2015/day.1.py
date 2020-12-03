#!/usr/bin/env python3

def execute():
    with open('2015/input/1.txt') as inp:
        lines = inp.readlines()
    return take_lift([l.strip() for l in lines if len(l.strip()) > 0][0])

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def take_lift(buttons):
    return buttons.count("(") - buttons.count(")")

def test_cases():
    verify(take_lift("(())"), 0)
    verify(take_lift("()()"), 0)
    verify(take_lift("((("), 3)
    verify(take_lift("(()(()("), 3)
    verify(take_lift("))((((("), 3)
    verify(take_lift("())"), -1)
    verify(take_lift("))("), -1)
    verify(take_lift(")))"), -3)
    verify(take_lift(")())())"), -3)

if __name__ == "__main__":
    test_cases()
    print(execute())