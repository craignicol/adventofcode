#!/usr/bin/env python3

def execute():
    with open('2022/input/day.9.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return tail_positions(data)[1], 6284, tail_positions(data, 9)[1]

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

sample_input2 = """
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""".splitlines()

def sign(x):
    if x == 0:
        return 0
    return x // abs(x)

def tail_positions(moves, tails = 1, animate = False):
    visited = set()
    moves.append("R 0")
    x = 0
    y = 0
    head = (x,y)
    tails = [(x,y) for i in range(tails)]
    visited.add(tails[-1])
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

            following = (x,y)
            new_tails = []
            for tail in tails:
            # move the tail based on where the head was
                xdiff, ydiff = following[0] - tail[0], following[1] - tail[1]
                if abs(xdiff) > 1 or abs(ydiff) > 1: 
                    tail = (tail[0] + sign(xdiff), tail[1] + sign(ydiff))
                following = tail    
                new_tails.append(tail)
            tails = new_tails
            visited.add(tails[-1])

            head = (x,y)
        if animate:
            print (move, head, tails)
    return visited, len(visited), [head] + tails

def plot_path(visited):
    height = min([y for x,y in visited]), max([y for x,y in visited])
    width = min([x for x,y in visited]), max([x for x,y in visited])
    for y in range(height[1]+1, height[0]-1, -1):
        for x in range(width[0]-1, width[1]+1):
            if (x,y) in visited:
                print("#", end="")
            else:
                print(".", end="")
        print()

def test_cases():
    verify(tail_positions([])[1],1)
    verify(tail_positions(sample_input)[1],13)
    plot_path(tail_positions(sample_input)[0])
    verify(tail_positions(sample_input, 9)[1],1)
    plot_path(tail_positions(sample_input, 9)[0])
    verify(tail_positions(sample_input2, 9)[1],36)
    plot_path(tail_positions(sample_input2, 9)[0])
    # verify(tail_positions(sample_input2, 9, True)[2], [])
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())