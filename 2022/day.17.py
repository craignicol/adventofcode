#!/usr/bin/env python3

def execute():
    with open('2022/input/day.17.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0][0]
    return len(data)

tests_failed = 0
tests_executed = 0

tetris_shapes = {
    '-': [[True, True, True, True]],
    '+':[[False, True, False], [True, True, True], [False, True, False]], 
    'J': [[False, False, True], [False, False, True], [True, True, True]], 
    '|': [[True], [True], [True], [True]],
    'o': [[True, True], [True, True]]}

sample_input = ">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"

def verify(a, b):
    global tests_executed
    global tests_failed

    tests_executed += 1
    if (a == b):
        print("✓")
        return
    
    tests_failed += 1
    print (locals())

def is_valid(grid, shape, position):
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                if position[1] + row < 0:
                    return False
                if position[1] + row >= len(grid):
                    return False
                if position[0] + col < 0:
                    return False
                if position[0] + col >= len(grid[0]):
                    return False
                if grid[position[1] + row][position[0] + col]:
                    return False
    return True

def add_shape_to_grid(grid, shape, position):
    if len(grid) <= position[1]:
        grid += [[False] * 7 for _ in range(position[1] + 1 - len(grid))]
    for row in range(len(shape)):
        for col in range(len(shape[row])):
            if shape[row][col]:
                grid[row + position[1]][col + position[0]] = True
    return grid

def add_shape(grid, data, shape, next_move):
    position = (2, len(grid) + 3)
    height = position[1]
    for row in range(height + 1, -1, -1):
        move = data[next_move]
        next_move = (next_move + 1) % len(data)
        if move == '>':
            new_position = (position[0] + 1, position[1])
        elif move == '<':
            new_position = (position[0] - 1, position[1])
        if is_valid(grid, shape, new_position):
            position = new_position
        new_position = (position[0], position[1] - 1)
        if is_valid(grid, shape, new_position):
            position = new_position
        if position != new_position:
            break
    return add_shape_to_grid(grid, shape, position), next_move

def draw_grid(grid):
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col]:
                print('#', end='')
            else:
                print('.', end='')
        print()

def height_after(data, drops):
    shape_order = "-+J|o"
    grid = []
    next_move = 0
    for drop in range(drops):
        shape = tetris_shapes[shape_order[drop % len(shape_order)]]
        grid, next_move = add_shape(grid, data, shape, next_move)
        draw_grid(grid)
    return len(grid)

def test_cases():    
    verify(height_after(sample_input, 1), 1)
    verify(height_after(sample_input, 2), 4)
    verify(height_after(sample_input, 3), 6)
    verify(height_after(sample_input, 2022), 3068)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())