#!/usr/bin/env python3

from math import log
from math import ceil

def execute():
    with open('input.12.txt') as inp:
        lines = inp.readlines()
    #interim =  sum_plant_position([l.strip() for l in lines if len(l.strip()) > 0], 2000) # 50000000000)
    return sum((x+50000000000-999) for x in [903, 910, 915, 924, 929, 934, 939, 944, 953, 958, 967, 972, 978, 989, 994, 999, 1004, 1009, 1014, 1019, 1024, 1029, 1040, 1049, 1054, 1059, 1068, 1073, 1078, 1083, 1086, 1093, 1098])

def sum_plant_position(program, generations):
    state = '...' + program[0][len('initial state: '):]
    state = sum([2**z[1] for z in zip(state, range(len(state))) if z[0] == '#'])
    offset = -3
    rules = dict([s.split(' => ') for s in program[1:] if len(s.strip()) > 0 and s[-1] == '#'])
    bitmask_rules = [sum([2**z[1] for z in zip(r, range(len(r))) if z[0] == '#']) for r in rules.keys()]
    print(bitmask_rules)

    for g in range(generations):
        gstate = None
        new_state = 0
        old_state = state
        i = 2**5
        addor = 4
        
        old_offset = offset
        
        while addor < state * 4:
            if old_state % i in bitmask_rules:
                #print(old_state, i, old_state % i)
                if addor == 4:
                    offset -= 1
                new_state += addor
            addor *= 2
            old_state //= 2 
        if old_offset > offset:
            new_state *= 2
        state = new_state
        if g % 1000 == 0:
            if gstate == None:
                gstate = state
                f = generations // 1000
                endstate = gstate << f
            pstate = ''.join(['.#'[(state & 2**c) > 0] for c in range(ceil(log(state, 2)))])
            idxs = [z[1] for z in zip(pstate, range(offset, len(pstate))) if z[0] == '#']

            print(g, idxs)

    state = ''.join(['.#'[(state & 2**c) > 0] for c in range(ceil(log(state, 2)))])
    return sum([z[1] for z in zip(state, range(offset, len(state))) if z[0] == '#'])


def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    test_input="""initial state: #..#.#..##......###...###

...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #"""
    verify(sum_plant_position(test_input.split('\n'), 20), 325)

if __name__ == "__main__":
    test_cases()
    print(execute())