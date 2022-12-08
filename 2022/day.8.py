#!/usr/bin/env python3

def execute():
    with open('2022/input/day.8.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return visible_trees(data)

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

tree_heights = """30373
25512
65332
33549
35390
""".splitlines()

def visible_trees(tree_heights):
    heights = [[int(t) for t in h] for h in tree_heights]
    visible = len(heights) * 2 + len(heights[0]) * 2 - 4 # 4 corners
    for i in range(1, len(heights)-1):
        for j in range(1, len(heights[i])-1):
            above = [heights[i-x][j] for x in range(1, i+1)]
            below = [heights[i+x][j] for x in range(1, len(heights)-i)]
            left = [heights[i][j-x] for x in range(1, j+1)]
            right = [heights[i][j+x] for x in range(1, len(heights[i])-j)]
            if heights[i][j] > max(above) or heights[i][j] > max(below) or heights[i][j] > max(left) or heights[i][j] > max(right):
                visible += 1                
    return visible

def test_cases():
    verify(visible_trees(tree_heights), 21)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())