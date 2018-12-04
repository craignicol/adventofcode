#!/usr/bin/env python3

def execute():
    with open('input.2.txt') as inp:
        lines = inp.readlines()
    return checksum(lines)

def count_letters(box_id):
    alphabet = [chr(i) for i in range(97,123)]
    counts = dict(zip(alphabet, [0]*len(alphabet)))
    for c in box_id:
        counts[c] += 1
    # print (counts)
    return 2 in counts.values(),3 in counts.values()

def checksum(box_ids):
    ids = [s.split()[0] for s in box_ids if len(s.strip()) > 0]
    doubles = 0
    triples = 0
    for box_id in ids:
        (has_double, has_triple) = count_letters(box_id)
        doubles += has_double
        triples += has_triple
    return doubles * triples

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    boxes = """
    abcdef contains no letters that appear exactly two or three times.
    bababc contains two a and three b, so it counts for both.
    abbcde contains two b, but no letter appears exactly three times.
    abcccd contains three c, but no letter appears exactly two times.
    aabcdd contains two a and two d, but it only counts once.
    abcdee contains two e.
    ababab contains three a and three b, but it only counts once.
    """
    verify(checksum(boxes.split("\n")), 12)

if __name__ == "__main__":
    test_cases()
    print(execute())