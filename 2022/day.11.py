#!/usr/bin/env python3

def execute():
    with open('2022/input/day.11.txt') as inp:
        lines = inp.readlines()
    data = parse_monkeys([l.strip() for l in lines])
    return len(data)

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

sample_input = """Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1
""".splitlines()

class Branch:
    def __init__(self, condition, iftrue, iffalse):
        self.condition = condition
        self.iftrue = iftrue
        self.iffalse = iffalse

    def __str__(self):
        return "Branch: {} ? {} : {}".format(self.condition, self.iftrue, self.iffalse)

class Monkey:
    def __init__(self, id, items, operation, test):
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test

    def __str__(self):
        return "Monkey {}: {} {} {}".format(self.id, self.items, "<lambda>", self.test)

def parse_monkeys(input):
    monkeys = []
    
    for line in input:
        if line.find("Monkey") > -1:
            id = int(line.split()[1][:-1])
            items = []
            operation = None
            condition = None
            iftrue = None
            iffalse = None
        elif line.find("Starting items:") > -1:
            items = [int(i) for i in line.split(":")[1].split(",")]
        elif line.find("Operation:") > -1:
            operation = eval("lambda old: " + line.split(": new = ")[1])
        elif line.find("Test:") > -1:
            condition = int(line.split(": divisible by ")[1].strip())
        elif line.find("If true:") > -1:
            iftrue = int(line.split(": throw to monkey ")[1].strip())
        elif line.find("If false:") > -1:
            iffalse = int(line.split(": throw to monkey ")[1].strip())
            test = Branch(condition, iftrue, iffalse)
        elif len(line.strip()) == 0:
            monkeys.append(Monkey(id, items, operation, test))
    monkeys.append(Monkey(id, items, operation, test))
    return monkeys

def test_cases():
    start = parse_monkeys(sample_input)
    verify(len(start), 4)
    verify(start[0].id, 0)
    verify(start[0].items, [79, 98])
    verify(start[0].operation(2), 38)
    verify(str(start[1]), "Monkey 1: [54, 65, 75, 74] <lambda> Branch: 19 ? 2 : 0")
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())