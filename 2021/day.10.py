#!/usr/bin/env python3

def execute():
    with open('./input/day.10.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return syntax_error_score(data)

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

scores = { ')': 3, ']': 57, '}':1197, '>': 25137 }

example1 = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]""".splitlines()

match_brackets = { '>' : '<', '<' : '>', ')' : '(', '(' : ')', ']' : '[', '[' : ']', '{' : '}', '}' : '{' }

def find_corrupted_chars(data):
    corrupted_chars = []
    for line in data:
        bracket_stack = []
        for i in line:
            if i in '<{([':
                bracket_stack.append(i)
            elif i in '>})]':
                if len(bracket_stack) == 0:
                    corrupted_chars.append(i)
                else:
                    opener = bracket_stack.pop()
                    if match_brackets[i] != opener:
                        corrupted_chars.append(i)
    return corrupted_chars

def syntax_error_score(data):
    corrupted_chars = find_corrupted_chars(data)
    return sum([scores[c] for c in corrupted_chars])

def test_cases():
    verify(syntax_error_score(example1), 26397)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())