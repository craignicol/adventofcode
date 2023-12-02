#!/usr/bin/env python3

import math


def execute():
    with open('2022/input/day.21.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return calculate_root(data), root_equality(data)

tests_failed = 0
tests_executed = 0

def verify(a, b):
    global tests_executed
    global tests_failed

    tests_executed += 1
    if (a == b):
        print("✓")
        return
    
    tests_failed += 1
    print (locals())

sample_input = """root: pppw + sjmn
dbpl: 5
cczh: sllz + lgvd
zczc: 2
ptdq: humn - dvpt
dvpt: 3
lfqf: 4
humn: 5
ljgn: 2
sjmn: drzm * dbpl
sllz: 4
pppw: cczh / lfqf
lgvd: ljgn * ptdq
drzm: hmdt - zczc
hmdt: 32"""

def parse_equation(equation):
    tokens = equation.split()
    if len(tokens) == 1:
        return int(tokens[0])
    else:
        return tokens

def parse_program(program):
    lines = [s.split(': ') for s in program]
    lines = [(l[0], parse_equation(l[1])) for l in lines]
    return dict(lines)

def aggregate(x, op, y):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        return x / y

def calculate(equation, program):
    if type(equation) != type([]): # number
        return equation    
    else:
        return aggregate(calculate(program[equation[0]], program), equation[1], calculate(program[equation[2]], program))

def calculate_root(program):
    ram = parse_program(program)
    return calculate(ram['root'], ram)

def find_humn(target, var, program):
    if var == 'humn':
        return target
    
    eq = program[var]
    if type(eq) == type([]):
        x,y = calculate(program[eq[0]], program), calculate(program[eq[2]], program)
        if math.isnan(x):
            if eq[1] == '+':
                return find_humn(target - y, eq[0], program) # target = ? + y
            elif eq[1] == '-':
                return find_humn(target + y, eq[0], program) # target = ? - y
            elif eq[1] == '*':
                return find_humn(target / y, eq[0], program) # target = ? * y
            elif eq[1] == '/':
                return find_humn(target * y, eq[0], program) # target = ? / y
        else:
            if eq[1] == '+':
                return find_humn(target - x, eq[2], program) # target = x + ?
            elif eq[1] == '-':
                return find_humn(x - target, eq[2], program) # target = x - ?
            elif eq[1] == '*':
                return find_humn(target / x, eq[2], program) # target = x * ?
            elif eq[1] == '/':
                return find_humn(x / target, eq[2], program) # target = x / ?
    return math.nan

def root_equality(program):
    ram = parse_program(program)
    root = ram['root']
    ram['humn'] = float('NaN')
    # Need to find value of humn that makes ram[0] == ram[2]
    x,y = calculate(ram[root[0]], ram), calculate(ram[root[2]], ram)
    if math.isnan(x):
        return find_humn(y, root[0], ram)
    else:
        return find_humn(x, root[2], ram)

def test_cases():
    verify(calculate_root(sample_input.splitlines()), 152)
    verify(root_equality(sample_input.splitlines()), 301)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())