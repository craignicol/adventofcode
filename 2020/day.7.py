#!/usr/bin/env python3

example_rules = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

def execute():
    with open('2020/input/7.txt') as inp:
        lines = inp.readlines()
    return count_parents(''.join(lines), "shiny gold")

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

def parse_child(child):
    (number, adj, colour, _) = child.split()
    return (adj+' '+colour, int(number))

def parse_rule(rule):
    # rule[-1] strips the trailing .
    parent, child_descriptions = rule[:-1].split(' bags contain ')
    children = [parse_child(c) for c in child_descriptions.split(', ') if child_descriptions != "no other bags"]
    return parent, children

def parse_ruleset(ruleset):
    rules = {}
    for rule in ruleset.splitlines():
        parent, children = parse_rule(rule)
        rules[parent] = children
    return invert_tree(rules)

def invert_tree(rule_tree):
    result = {}
    for parent in rule_tree:
        children = rule_tree[parent]
        if parent not in result:
            result[parent] = []
        for child in children:
            (id, _) = child
            if id not in result:
                result[id] = []
            result[id].append(parent)
    return result

def find_parents(parent_rules, bag_id):
    if bag_id not in parent_rules:
        return []
    found = set(parent_rules[bag_id])
    for parent in parent_rules[bag_id]:
        found.update(find_parents(parent_rules, parent))
    return found

def count_parents(ruleset, bag_id):
    rule_tree = parse_ruleset(ruleset)
    return len(find_parents(rule_tree, bag_id))

def test_cases():
    verify(count_parents(example_rules, "shiny gold"), 4)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())