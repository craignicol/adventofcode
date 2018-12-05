#!/usr/bin/env python3

def execute():
    with open('input.3.txt') as inp:
        lines = inp.readlines()
    return overlapping_area([l.strip() for l in lines if len(l.strip()) > 0])

def print_fabric(fabric, limit = 15, quiet = True):
    if quiet:
        return
    for r in fabric[:limit]:
        for c in r[:limit]:
            print('X' if c == 1 else 'c' if c == 0 else '.', end = '')
        print()

def overlapping_area(claims):
    row = [None] * 1500
    fabric = [row[:] for i in range(1500)]
    
    for c in claims:
        print_fabric(fabric)
        (claim_id, topleft, size) = c.replace(':', '').replace('@', '').split()
        (left, top) = topleft.split(',')
        (top, left) = int(top), int(left)
        (width, height) = size.split('x')
        (width, height) = int(width), int(height)
        # print(claim_id, left, top, width, height)
        for x in range(left, left+width):
            for y in range(top, top+height):
                if fabric[x][y] == None:
                    fabric[x][y] = 0
                elif fabric[x][y] == 0:
                    fabric[x][y] = 1
    
    print_fabric(fabric)
        
    return sum([sum(filter(None, r)) for r in fabric])

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    claims = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""
    verify(overlapping_area(claims.split('\n')), 4)

if __name__ == "__main__":
    test_cases()
    print(execute())