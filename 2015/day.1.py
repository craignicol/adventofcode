#!/usr/bin/env python3

def execute():
    with open('2015/input/1.txt') as inp:
        lines = inp.readlines()
    buttons = [l.strip() for l in lines if len(l.strip()) > 0][0]
    return take_lift(buttons), steps_to_basement(buttons)

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def steps_to_basement(buttons):
    current_floor = 0
    current_step = 0
    for b in buttons:
        if current_floor < 0:
            return current_step
        if b == "(":
            current_floor += 1
        if b == ")":
            current_floor -= 1
        current_step += 1
    return current_step

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
    verify(steps_to_basement(")"), 1)
    verify(steps_to_basement("()())"), 5)
    verify(steps_to_basement("()())((((((("), 5)
    verify(steps_to_basement("()()))))))))"), 5)

if __name__ == "__main__":
    test_cases()
    print(execute())