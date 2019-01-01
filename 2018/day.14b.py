#!/usr/bin/env python3

from collections import deque

def execute():
    return first_appears(768071)

def first_appears(sequence):
    sequence = str(sequence)
    recipes = deque()
    recipes.append(3)
    recipes.append(7)
    elf1 = 0
    elf2 = 1
    while ''.join([str(recipes[i]) for i in range(-min(len(sequence)+1, len(recipes)), 0)]).find(sequence) == -1:
        # print (','.join(str(r) for r in recipes), ''.join([str(recipes[i]) for i in range(-min(len(sequence), len(recipes)), 0)]))
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
    return len(recipes) - len(sequence)

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    verify((first_appears('51589')), 9)
    verify((first_appears('01245')), 5)
    verify((first_appears('92510')), 18)
    verify((first_appears('59414')), 2018)

if __name__ == "__main__":
    test_cases()
    print(execute())