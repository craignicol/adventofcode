#!/usr/bin/env python3

def execute():
    with open('./input/day.2.txt') as inp:
        lines = inp.readlines()
    return distance_product([l.strip() for l in lines if len(l.strip()) > 0])

tests_failed = 0
tests_executed = 0

example1 = """forward 5
down 5
forward 8
up 3
down 8
forward 2""".splitlines()

def verify(a, b):
    global tests_executed
    global tests_failed

    tests_executed += 1
    if (a == b):
        print("✓")
        return
    
    tests_failed += 1
    print (locals())

move_fn = {
    "forward": lambda x, y, n : (x+n, y),
    "up": lambda x, y, n : (x, y-n),
    "down": lambda x, y, n : (x, y+n),
}

def follow_path(moves):
    x, y = 0,0
    for m in moves:
        (dn, size) = m.split()
        size = int(size)
        x, y = move_fn[dn](x, y, size)
    return (x,y)

def distance_product(moves):
    x, y = follow_path(moves)
    return x * y

def test_cases():
    verify(distance_product(example1), 150)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())