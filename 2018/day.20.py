#!/usr/bin/env python3

def execute():
    with open('input.20.txt') as inp:
        lines = inp.readlines()
    return longest_path([l.strip() for l in lines if len(l.strip()) > 0][0])

def longest_path(regex):
    return len(longest_subpath(regex.replace('^', '').replace('$', '')))

def collapse_branches(regex):
    bracket_stack = []
    branch = ''
    result = ''
    idx = 2
    for c in regex:
        if c == '(':
            if len(branch) > 0 and len(bracket_stack) > 0:
                #print(branch, bracket_stack, idx)
                if idx >= len(bracket_stack[-1]):
                    bracket_stack[-1].append(branch)
                else:
                    bracket_stack[-1][idx] += branch
            elif len(branch) > 0:
                result += branch
            branch = ''
            bracket_stack.append([c, idx, '', ''])
            idx = 2
        elif c == '|':
            if idx >= len(bracket_stack[-1]):
                bracket_stack[-1].append(branch)
            else:
                bracket_stack[-1][idx] += branch
            branch = ''
            idx += 1
        elif c == ')':
            if idx >= len(bracket_stack[-1]):
                bracket_stack[-1].append(branch)
            else:
                bracket_stack[-1][idx] += branch
            chosen = ''
            [_, idx, *opts] = bracket_stack.pop()
            options = sorted(opts, key=lambda s : len(s))
            if len(options[0]) > 0:
                chosen = options[-1]
            if len(bracket_stack) == 0:
                result += chosen
            else:
                bracket_stack[-1][idx] += chosen
            branch = ''
        else:
            branch += c
        # print(bracket_stack)
    return result + branch

def longest_subpath(regex):    
    if '(' not in regex:
        return regex
    else:
        left = regex.find('(')
        return regex[:left] + collapse_branches(regex[left:])

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    verify(longest_path("^WNE$"), 3)
    verify(longest_path("^ENWWW(NEEE|SSE(EE|N))$"), 10)
    verify(longest_path("^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"), 18)
    verify(longest_path("^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"), 23)
    verify(longest_path("^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"), 31)
    
if __name__ == "__main__":
    test_cases()
    print(execute())