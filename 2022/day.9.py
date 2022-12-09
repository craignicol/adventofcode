#!/usr/bin/env python3

def execute():
    with open('2022/input/day.9.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return tail_positions(data)[1]

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

sample_input = """
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2""".splitlines()

visited = set()

def sign(x):
    if x == 0:
        return 0
    return x // abs(x)

def tail_positions(moves):
    x = 0
    y = 0
    head = (x,y)
    tail = (x,y)
    visited.add(tail)
    for move in moves:
        if len(move.strip()) == 0:
            continue
        move = move.split()
        direction = move[0]
        distance = int(move[1])
        for i in range(distance):
            # move the head
            if direction == "R":
                x += 1
            elif direction == "L":
                x -= 1
            elif direction == "U":
                y += 1
            elif direction == "D":
                y -= 1

            # move the tail based on where the head was
            xdiff, ydiff = head[0] - tail[0], head[1] - tail[1]
            if abs(xdiff) > 1 or abs(ydiff) > 1: 
                tail = (tail[0] + sign(xdiff), tail[1] + sign(ydiff))
                visited.add(tail)

            head = (x,y)
    return visited, len(visited)

def plot_path(visited):
    height = max([y for x,y in visited])
    width = max([x for x,y in visited])
    height, width = max([height, width]), max([height, width])
    for y in range(height, -1, -1):
        for x in range(0, width+2):
            if (x,y) in visited:
                print("#", end="")
            else:
                print(".", end="")
        print()

def test_cases():
    verify(tail_positions([])[1],1)
    verify(tail_positions(sample_input)[1],13)
    plot_path(tail_positions(sample_input)[0])
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())