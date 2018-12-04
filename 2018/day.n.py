#!/usr/bin/env python3

def execute():
    with open('input.1.txt') as inp:
        lines = inp.readlines()
    return len(lines)

if __name__ == "__main__":
    print(execute())