#!/usr/bin/env python3

def execute():
    with open('./input/day.2.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return distance_product(data, direct_move), distance_product(data, aim_move)

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

direct_move = {
    "forward": lambda x, y, z, n : (x+n, y, z),
    "up": lambda x, y, z, n : (x, y-n, z),
    "down": lambda x, y, z, n : (x, y+n, z),
}

aim_move = {
    "forward": lambda x, y, z, n : (x+n, y+(z*n), z),
    "up": lambda x, y, z, n : (x, y, z-n),
    "down": lambda x, y, z, n : (x, y, z+n),
}

def follow_path(moves, move_fn):
    x, y, z = 0,0,0
    for m in moves:
        (dn, size) = m.split()
        size = int(size)
        x, y, z = move_fn[dn](x, y, z, size)
    return (x,y)

def distance_product(moves, move_fn):
    x, y = follow_path(moves, move_fn)
    return x * y

def test_cases():
    verify(distance_product(example1, direct_move), 150)
    verify(distance_product(example1, aim_move), 900)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())