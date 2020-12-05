#!/usr/bin/env python3

def execute():
    with open('2015/input/2.txt') as inp:
        lines = inp.readlines()
    return total_area_of_wrapping_paper([l.strip() for l in lines if len(l.strip()) > 0])

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

def area_of_box(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l

def min_side(l, w, h):
    return (l*w*h)/max(l,w,h)

def area_of_wrapping_paper(dimensions):
    (l,w,h) = [int(d) for d in dimensions.split("x")]
    return area_of_box(l, w, h) + min_side(l, w, h)

def total_area_of_wrapping_paper(all_boxes):
    return sum(area_of_wrapping_paper(box) for box in all_boxes)

def test_cases():
    verify(area_of_wrapping_paper("2x3x4"), 58)
    verify(area_of_wrapping_paper("1x1x10"), 43)
    verify(total_area_of_wrapping_paper(["2x3x4", "1x1x10"]), 101)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())