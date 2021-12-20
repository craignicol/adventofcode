#!/usr/bin/env python3

from collections import defaultdict
from typing import DefaultDict


def execute():
    with open('./input/day.14.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return len(data)

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

example1 = """NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C""".splitlines()

def parse_polymer(lines):
    polymer = lines[0]

    rules = {}
    for line in lines[2:]:
        a, b = line.split(' -> ')
        d = defaultdict(int)
        d[b] += 1
        rules[a] = {'insert':b, 'counts':d}

    return polymer, rules

### {NN : C; NC: N; CN: N}
### {NN : {C:1}; NC: {N:1}; CN: {N:1}}
### {NN : {C:1, N:2}; NC: {N:2,C:1}; CN: {N:2,C:1}}
### i.e. NN : d[NN] + d[NC] + d[CN]

def merge_counts(counts1, counts2):
    for k in counts2.keys():
        counts1[k] += counts2[k]
    return counts1

def run_step(polymer_rules):
    polymer, rules = polymer_rules
    new_rules = {}
    for k in rules.keys():
        v = defaultdict(int, rules[k].copy()) # deepcopy
        new_rules[k] = {'insert':v['insert'], 'counts':v['counts'].copy()}
        merge_counts(new_rules[k]['counts'], rules[k[0] + v['insert']]['counts'])
        merge_counts(new_rules[k]['counts'], rules[v['insert'] + k[1]]['counts'])
    return polymer, new_rules

def run_steps(polymer_rules, steps):
    for _ in range(steps):
        polymer_rules = run_step(polymer_rules)
    return polymer_rules

def score(polymer_rules):
    polymer, rules = polymer_rules
    counts = defaultdict(int)
    for i in range(len(polymer) - 1):
        next = polymer[i:i+2]
        merge_counts(counts, rules[next]['counts'])
    if len(counts) == 0:
        return 0
    return max(counts.values()) - min(counts.values())

def test_cases():
    verify(score(parse_polymer(example1)), 1)
    verify(score(run_steps(parse_polymer(example1), 1)), 1)
    verify(score(run_steps(parse_polymer(example1), 10)), 1588)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())