#!/usr/bin/env python3

def execute():
    with open('input.15.txt') as inp:
        lines = inp.readlines()
    return len([l.strip() for l in lines if len(l.strip()) > 0])

units = []
world = []

def get_unit_locations(grid):
    units = []
    y = 0
    for row in grid:
        x = 0
        for ch in row:
            if ch in ['E', 'G']:
                units.append((x,y,ch,200))
            x += 1
        y += 1
    return units

def remove_units(grid):
    return [r.replace('G','.').replace('E', '.').replace('\n', '') for r in grid]

def sorted_units(units):
    return sorted(units, key=lambda x: x[0] + 1000 * x[1])

def unit_at(x, y):
    return len([(tx, ty) for (tx, ty, _, _) in units if x == tx and y == ty]) > 0

def get_units(ch):
    return [u for u in units if u[2] == ch]

def move(unit):
    targets = get_units('E') if unit[2] == 'G' else get_units('G')
    
    pass

def attack(unit, enemy):
    enemy[3] -= 3

def final_score(start):
    units = get_unit_locations(start)
    world = remove_units(start)
    rounds = 0
    while len(get_units('E')) > 0:
        for u in units:
            move(u)
            attack(u)
        units = sorted_units([u for u in units if u[3] > 0])
    return len(units), rounds

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

test1 = """#######
#.G...#
#...EG#
#.#.#G#
#..G#E#
#.....#
#######"""

test2 = """#######
#G..#E#
#E#E.E#
#G.##.#
#...#E#
#...E.#
#######"""

test3 = """#######
#E..EG#
#.#G.E#
#E.##E#
#G..#.#
#..E#.#
#######"""

test4 = """#######
#E.G#.#
#.#G..#
#G.#.G#
#G..#.#
#...E.#
#######"""

test5 = """#######
#.E...#
#.#..G#
#.###.#
#E#G#G#
#...#G#
#######"""

test6 = """#########
#G......#
#.E.#...#
#..##..G#
#...##..#
#...#...#
#.G...G.#
#.....G.# 
#########"""

def test_cases():
    verify(final_score(test1.splitlines()), 27730)
    verify(final_score(test2.splitlines()), 36334)
    verify(final_score(test3.splitlines()), 39514)
    verify(final_score(test4.splitlines()), 27755)
    verify(final_score(test5.splitlines()), 28944)
    verify(final_score(test6.splitlines()), 18740)

if __name__ == "__main__":
    test_cases()
    print(execute())