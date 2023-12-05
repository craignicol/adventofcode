#!/usr/bin/env python3

def execute():
    with open('2023/input/day.3.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return sum(part_numbers(data))

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

def find_symbols(line):
    locations = []
    for idx, c in enumerate(line):
        if c not in '0123456789.':
            locations.append(idx)
    return set(locations)

def find_adjacent_numbers(line, symbols):
    numbers = []
    current = 0
    near_symbol = False
    in_number = False
    sym = symbols[0].union(symbols[1]).union(symbols[2])

    for idx, c in enumerate(line):
        if in_number:
            near_symbol = near_symbol or (idx in sym) 
        if c not in '0123456789':
            if near_symbol and in_number:
                numbers.append(current)
            current = 0
            in_number = False
            near_symbol = False
        else:
            current = (current * 10) + int(c)
            if not in_number:
                in_number = True
                near_symbol = near_symbol or ((idx-1) in sym) or (idx in sym) or ((idx + 1) in sym)
    if near_symbol and in_number and current > 0:
        numbers.append(current)
    return numbers

def part_numbers(inp):
    numbers = []
    symbols = [set(),find_symbols(inp[0]),find_symbols(inp[1])]
    for idx, line in enumerate(inp):
        numbers.extend(find_adjacent_numbers(line, symbols))
        symbols = [symbols[1], symbols[2], find_symbols(inp[idx+2]) if idx < (len(inp) - 2) else set()]
    return numbers

sample_input = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""

def test_cases():
    inp = sample_input.splitlines()
    verify(part_numbers(inp), [467, 35, 663, 617, 592, 755, 664, 598])
    verify(sum(part_numbers(inp)), 4361)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())