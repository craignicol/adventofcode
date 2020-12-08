#!/usr/bin/env python3

example_input = """123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i"""

def execute():
    with open('2015/input/7.txt') as inp:
        lines = inp.readlines()
    return emulate([l.strip() for l in lines if len(l.strip()) > 0])

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

def get_value(maybe_var, wires):
    if maybe_var in wires:
        return wires[maybe_var]
    if maybe_var.isdigit():
        return int(maybe_var)
    return 0

operators = {
    "AND": (lambda a,b: a & b),
    "OR": (lambda a,b: a | b),
    "LSHIFT": (lambda a,b: a << b),
    "RSHIFT": (lambda a,b: a >> b),
}

def evaluate(expression,wires):
    expression = expression.split()
    if len(expression) == 1:
        return get_value(expression[0], wires)
    if len(expression) == 2 and expression[0] == "NOT":
        return ~get_value(expression[1], wires)
    if len(expression) == 3:
        (lhs, operator, rhs) = expression
        return operators[operator](get_value(lhs, wires), get_value(rhs, wires))
        
    return None

def emulate(program):
    wires = {c:0 for c in "abcdefghijklmnopqrstuvwxyz"}
    for i in range(len(program)):
        for op in program:
            (expression, target) = op.split(" -> ")
            wires[target] = evaluate(expression, wires) % 65536
    return wires

def test_cases():
    output = emulate(example_input.splitlines())
    verify(output["d"], 72)
    verify(output["e"], 507)
    verify(output["f"], 492)
    verify(output["g"], 114)
    verify(output["h"], 65412)
    verify(output["i"], 65079)
    verify(output["x"], 123)
    verify(output["y"], 456)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())