#!/usr/bin/env python3

def execute():
    with open('2022/input/day.13.txt') as inp:
        lines = inp.readlines()
    data = [l for l in lines]
    return check_order(data)[1]

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

sample_input = """[1,1,3,1,1]
[1,1,5,1,1]

[[1],[2,3,4]]
[[1],4]

[9]
[[8,7,6]]

[[4,4],4,4]
[[4,4],4,4,4]

[7,7,7,7]
[7,7,7]

[]
[3]

[[[]]]
[[]]

[1,[2,[3,[4,[5,6,7]]]],8,9]
[1,[2,[3,[4,[5,6,0]]]],8,9]
""".splitlines()

def is_ordered(first, second):
    for i in range(len(first)):
        if i >= len(second):
            return False
        if type(first[i]) == int and type(second[i]) == int:
            if first[i] != second[i]:
                return first[i] < second[i]
        elif type(first[i]) == list and type(second[i]) == list:
            if not is_ordered(first[i], second[i]):
                return False
        elif type(first[i]) == int and type(second[i]) == list:
            if not is_ordered([first[i]], second[i]):
                return False
        elif type(first[i]) == list and type(second[i]) == int:
            if not is_ordered(first[i], [second[i]]):
                return False
    return True

def check_order(input):
    is_in_order = [False]
    first, second = None, None
    for line in input:
        if line.startswith("["):
            if first is None:
                first = eval(line)
            elif second is None:
                second = eval(line)
        if line.strip() == "":
            is_in_order.append(is_ordered(first, second))
            first, second = None, None
    is_in_order.append(is_ordered(first, second)) # EOL
                
    return is_in_order, sum([x for x, i in enumerate(is_in_order) if i])

def test_cases():
    is_in_order, score = check_order(sample_input)
    verify(len(is_in_order), 9)
    verify(is_in_order[1], True)
    verify(is_in_order[2], True)
    verify(is_in_order[3], False)
    verify(is_in_order[4], True)
    verify(is_in_order[5], False)
    verify(is_in_order[6], True)
    verify(is_in_order[7], False)
    verify(is_in_order[8], False)
    verify(score, 13)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())