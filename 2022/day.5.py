#!/usr/bin/env python3

def execute():
    with open('2022/input/day.5.txt') as inp:
        lines = inp.readlines()
    data = [l for l in lines if len(l.strip()) > 0]
    return move_crates(data)[1], move_crates9001(data)[1]

tests_failed = 0
tests_executed = 0

sample_input = """
    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".splitlines()

def verify(a, b):
    global tests_executed
    global tests_failed

    tests_executed += 1
    if (a == b):
        print("✓")
        return
    
    tests_failed += 1
    print (locals())

def parse_input(input):
    moves = []
    crate_spec = []
    crates = [[]]
    columns = 0

    for line in input:
        if line.startswith("move"):
            moves.append(line)
        elif line.find("[") >= 0:
            crate_spec.append(line + " ")
        elif line.startswith(" 1"):
            columns = max(int(p) for p in line.split())
            crates = [[] for i in range(columns)]
    for s in crate_spec:
        for c in range(len(s)//4):
            maybe_crate = s[c*4:(c+1)*4]
            if maybe_crate[0] == "[":
                crates[c].insert(0, maybe_crate[1])
    return crates, moves

def move_crates(input):
    crates, moves = parse_input(input)
    for move in moves:
        _, count, _, start, _, end = move.split()
        for i in range(int(count)):
            crates[int(end)-1].append(crates[int(start)-1].pop())
    return crates, ''.join([c[-1] for c in crates if len(c) > 0])

def move_crates9001(input):
    crates, moves = parse_input(input)
    for move in moves:
        _, count, _, start, _, end = move.split()
        crates[int(end)-1].extend(crates[int(start)-1][-int(count):])
        for i in range(int(count)):
            crates[int(start)-1].pop()
    return crates, ''.join([c[-1] for c in crates if len(c) > 0])


def test_cases():
    verify(parse_input(sample_input)[0], [['Z', 'N'], ['M', 'C', 'D'], ['P']])
    verify(move_crates(sample_input)[1], "CMZ")
    verify(move_crates9001(sample_input)[1], "MCD")
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())