#!/usr/bin/env python3

def execute():
    with open('input.8.txt') as inp:
        lines = inp.readlines()
    return checksum([l.strip() for l in lines if len(l.strip()) > 0][0])

def extract_metadata(tree, siblings = 1):
    children = int(tree[0])
    metadata_count = int(tree[1])
    remainder = tree[2:]
    
    total = 0
    
    for c in range(children):
        (subtotal, remainder) = extract_metadata(remainder, children)
        total += subtotal
    
    total += sum(int(i) for i in remainder[:metadata_count])

    return (total, remainder[metadata_count:])

def checksum(tree):
    return extract_metadata(tree.split())[0]

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    verify(checksum("2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2"), 138)

if __name__ == "__main__":
    test_cases()
    print(execute())