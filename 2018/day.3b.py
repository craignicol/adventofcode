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
            print(c, end = ' ')
        print()

def overlapping_area(claims):
    row = [None] * 1500
    fabric = [row[:] for i in range(1500)]
    
    overlapping = {}
    claim_ids = []
    
    for c in claims:
        print_fabric(fabric)
        (claim_id, topleft, size) = c.replace(':', '').replace('@', '').split()
        claim_ids.append(claim_id)
        (left, top) = topleft.split(',')
        (top, left) = int(top), int(left)
        (width, height) = size.split('x')
        (width, height) = int(width), int(height)
        # print(claim_id, left, top, width, height)
        for x in range(left, left+width):
            for y in range(top, top+height):
                if fabric[x][y] == None:
                    fabric[x][y] = claim_id
                else: 
                    overlapping[claim_id] = True
                    overlapping[fabric[x][y]] = True
                    fabric[x][y] = 'x' + fabric[x][y][1:]
                    overlapping[claim_id] = True
                    overlapping[fabric[x][y]] = True
    
    print_fabric(fabric)
        
    return [c for c in claim_ids if c not in overlapping.keys()]

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    claims = """#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2"""
    verify(overlapping_area(claims.split('\n'))[0], '#3')

if __name__ == "__main__":
    test_cases()
    print(execute())