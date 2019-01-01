#!/usr/bin/env python3

def execute():
    with open('input.23.txt') as inp:
        lines = inp.readlines()
    return nanobots_in_range([l.strip() for l in lines if len(l.strip()) > 0])

def parse_bot(b):
    (pos, r) = b.split('>, r=')
    r = int(r)
    (x,y,z) = [int(p) for p in pos[5:].split(',')]
    return ((x,y,z), r)

def parse_bots(inp):
    return [parse_bot(b) for b in inp]

def manhatten(p1, p2):
    (x1, y1, z1) = p1
    (x2, y2, z2) = p2
    return abs(x1-x2) + abs(y1-y2) + abs(z1-z2)

def nanobots_in_range(inp):
    nanobots = parse_bots(inp)
    nanobots = sorted(nanobots, key=lambda r: r[1])
    (origin, radius) = nanobots[-1]
    in_range = [n for n in nanobots if manhatten(origin, n[0]) <= radius]
    return len(nanobots), (origin, radius), len(in_range)

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    inp = """pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1"""
    verify(nanobots_in_range(inp.splitlines()), 7)

if __name__ == "__main__":
    test_cases()
    print(execute())