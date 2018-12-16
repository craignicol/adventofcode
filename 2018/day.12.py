#!/usr/bin/env python3

def execute():
    with open('input.12.txt') as inp:
        lines = inp.readlines()
    return sum_plant_position([l.strip() for l in lines if len(l.strip()) > 0], 20)

def sum_plant_position(program, generations):
    state = '...' + program[0][len('initial state: '):] + '...'
    offset = -3
    rules = dict([s.split(' => ') for s in program[2:] if s[-1] == '#'])
    
    for _ in range(generations):
        new_state = '..'
        for i in range(2, len(state) - 2):
            if state[i-2:i+3] in rules:
                if i == 2:
                    new_state += '.'
                    offset -= 1
                new_state += '#'
                if i == len(state) - 3:
                    new_state += '.'
            else:
                new_state += '.'
        state = new_state + '..'
    
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