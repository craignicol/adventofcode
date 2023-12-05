#!/usr/bin/env python3

import math


def execute():
    with open('2023/input/day.4.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return total_score(data)

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

sample_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"""

def score(card):
    id, game = card.split(':')
    win, mine = game.split('|')
    win = set(win.split())
    mine = set(mine.split())
    return math.floor(2 ** (len(win.intersection(mine)) - 1))

def total_score(cards):
    return sum([score(card) for card in cards])

def test_cases():
    inp = sample_input.splitlines()
    verify(score(inp[0]), 8)
    verify(score(inp[1]), 2)
    verify(score(inp[2]), 2)
    verify(score(inp[3]), 1)
    verify(score(inp[4]), 0)
    verify(score(inp[5]), 0)
    verify(total_score(inp), 13)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())