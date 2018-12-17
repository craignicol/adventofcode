#!/usr/bin/env python3

from collections import deque

def execute():
    with open('input.1.txt') as inp:
        lines = inp.readlines()
    return next_10_recipes_after(768071)

def next_10_recipes_after(n):
    recipes = deque()
    recipes.append(3)
    recipes.append(7)
    elf1 = 0
    elf2 = 1
    while len(recipes) < n + 10:
        new_recipe = recipes[elf1] + recipes[elf2]
        if new_recipe < 10:
            recipes.append(new_recipe)
        else:
            recipes.append(new_recipe // 10)
            recipes.append(new_recipe % 10)
        elf1 += 1 + recipes[elf1]
        elf1 %= len(recipes)
        elf2 += 1 + recipes[elf2]
        elf2 %= len(recipes)
    return ''.join([str(recipes[i]) for i in range(n, n+10)])

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    verify((next_10_recipes_after(9)), '5158916779')
    verify((next_10_recipes_after(5)), '0124515891')
    verify((next_10_recipes_after(18)), '9251071085')
    verify((next_10_recipes_after(2018)), '5941429882')

if __name__ == "__main__":
    test_cases()
    print(execute())