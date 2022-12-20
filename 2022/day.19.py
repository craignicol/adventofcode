#!/usr/bin/env python3

import re


def execute():
    with open('2022/input/day.19.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return len(data)

tests_failed = 0
tests_executed = 0

sample_input = """Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian.
Blueprint 2: Each ore robot costs 2 ore. Each clay robot costs 3 ore. Each obsidian robot costs 3 ore and 8 clay. Each geode robot costs 3 ore and 12 obsidian.
""".splitlines()

def parse_blueprints(lines):
    regex = re.compile(r'Blueprint (\d+): Each ore robot costs (\d+) ore\. Each clay robot costs (\d+) ore\. Each obsidian robot costs (\d+) ore and (\d+) clay\. Each geode robot costs (\d+) ore and (\d+) obsidian\.')
    blueprints = {}
    for line in lines:
        m = regex.match(line)
        name, orebot, claybot, obsbotore, obsbotclay, geobotore, geobotobs = m.groups()
        blueprints[int(name)] = {
            'ore': [(int(orebot), 'ore')],
            'clay': [(int(claybot), 'ore')],
            'obsidian': [(int(obsbotore), 'ore'), (int(obsbotclay), 'clay')],
            'geode': [(int(geobotore), 'ore'), (int(geobotobs), 'obsidian')]
            }
    return blueprints

def verify(a, b):
    global tests_executed
    global tests_failed

    tests_executed += 1
    if (a == b):
        print("✓")
        return
    
    tests_failed += 1
    print (locals())

def test_cases():
    blueprints = parse_blueprints(sample_input)
    verify(blueprints[1]['ore'], [(4, 'ore')])
    verify(blueprints[2]['geode'], [(3, 'ore'), (12, 'obsidian')])
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())