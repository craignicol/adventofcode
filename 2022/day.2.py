#!/usr/bin/env python3

def execute():
    with open('./input/day.2.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return total_score(data)

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

example_plan = """A Y
B X
C Z""".splitlines()

my_score = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

battle_result = {
    "A": {
        "X": 3,
        "Y": 6,
        "Z": 0,
    },
    "B": {
        "X": 0,
        "Y": 3,
        "Z": 6,
    },
    "C": {
        "X": 6,
        "Y": 0,
        "Z": 3,
    }
}

def score_for_round(theirs, mine):
    score = 0
    score += my_score[mine]
    score += battle_result[theirs][mine]
    return score

def total_score(plan):
    return sum(score_for_round(*row.split()) for row in plan)

def test_cases():
    verify(score_for_round("A", "Y"), 8)
    verify(score_for_round("B", "X"), 1)
    verify(score_for_round("C", "Z"), 6)
    verify(total_score(example_plan), 15)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())