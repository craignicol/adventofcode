#!/usr/bin/env python3

def execute():
    with open('./input/day.13.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
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

example1 = """6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5""".splitlines()

def parse_origami(lines):
    dots = set()
    folds = []
    for line in lines:
        if line.count(',') == 1:
            dots.add(tuple(map(int, line.split(','))))
        elif line.startswith('fold'):
            folds.append(line.split(' ')[-1].split('='))
    return dots, folds

def fold_paper(origami):
    dots, folds = origami
    new_dots = set()
    for (axis, pos) in folds:
        for (x,y) in dots:
            pos = int(pos)
            if axis == 'y':
                new_dots.add((x, y if y < pos else pos + pos - y))
            elif axis == 'x':
                new_dots.add((x if x < pos else pos + pos - x, y))
        dots = new_dots
        new_dots = set()
    return dots, folds

def count_dots(origami):
    dots, _ = origami
    return len(dots)

def test_cases():
    verify(count_dots(parse_origami(example1)), 18)
    verify(count_dots(fold_paper(parse_origami(example1))), 17)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())