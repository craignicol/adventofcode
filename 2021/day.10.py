#!/usr/bin/env python3

def execute():
    with open('./input/day.10.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return syntax_error_score(data), autocomplete_score(data)

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

def compiler(data):
    corrupted_chars = []
    autocomplete = []
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
                        bracket_stack = [] # Can't autocomplete
                        break
        autocomplete.append(''.join([match_brackets[b] for b in bracket_stack[::-1]]))
    return corrupted_chars, autocomplete

def syntax_error_score(data):
    corrupted_chars, _ = compiler(data)
    return sum([scores[c] for c in corrupted_chars])

ascore = {')': 1, ']': 2, '}': 3, '>': 4}

def acscore(c):
    score = 0
    for b in c:
        score *= 5
        score += ascore[b]
    return score 

def autocomplete_score(data):
    _, autocomplete = compiler(data)
    line_scores =  [acscore(c) for c in autocomplete if len(c) > 0]
    # find median
    line_scores.sort()
    return line_scores[len(line_scores) // 2]

def test_cases():
    verify(syntax_error_score(example1), 26397)
    verify(compiler(example1[0:1])[1], ['}}]])})]'])
    verify(autocomplete_score(example1), 288957)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())