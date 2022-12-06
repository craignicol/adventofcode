#!/usr/bin/env python3

def execute():
    with open('2022/input/day.6.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return find_marker(data[0]), find_marker(data[0], 14)

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

"""Find marker in a string of characters.
The marker is a string of 4 unique characters."""
def find_marker(s, count=4):
    # Find the first 4 unique characters
    marker = s[:count]
    pos = count
    if (len(set(marker)) == count):
        return pos
    for c in s[count:]:
        pos += 1
        marker = marker[1:] + c
        if (len(set(marker)) == count):
            return pos
    return pos

def test_cases():
    verify(find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb"), 7)
    verify(find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz"), 5)
    verify(find_marker("nppdvjthqldpwncqszvftbrmjlhg"), 6)
    verify(find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"), 10)
    verify(find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"), 11)
    verify(find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14), 19)
    verify(find_marker("bvwbjplbgvbhsrlpgdmjqwftvncz", 14), 23)
    verify(find_marker("nppdvjthqldpwncqszvftbrmjlhg", 14), 23)
    verify(find_marker("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 14), 29)
    verify(find_marker("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 14), 26)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())