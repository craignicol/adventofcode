#!/usr/bin/env python3

def execute():
    with open('./input/day.9.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return summed_risk(data)

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

example1 = """2199943210
3987894921
9856789892
8767896789
9899965678""".splitlines()

def low_points(map):
    # surround with 9s to make calculations easier
    heights = [[9] + [int(i) for i in l] + [9] for l in map]
    header = [9] * (len(heights[0]))
    heights.insert(0, header)
    heights.append(header)
    result = []
    for i in range(1, len(heights) - 1):
        for j in range(1, len(heights[0]) - 1):
            if heights[i][j] < heights[i-1][j] and heights[i][j] < heights[i+1][j] and heights[i][j] < heights[i][j-1] and heights[i][j] < heights[i][j+1]:
                result.append(heights[i][j])
    return result

def summed_risk(data):
    l = low_points(data)
    return sum(l) + len(l)

def test_cases():
    verify(low_points(example1), [1,0,5,5])
    verify(summed_risk(example1), 15)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())