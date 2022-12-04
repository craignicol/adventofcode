#!/usr/bin/env python3

def execute():
    with open('2022/input/day.2.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return total_score(data), total_score_to_result(data)

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

score_for_result = {
    "X": 0,
    "Y": 3,
    "Z": 6,
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

choose_throw = {
    "A": {
        "X": "Z",
        "Y": "X",
        "Z": "Y",
    },
    "B": {
        "X": "X",
        "Y": "Y",
        "Z": "Z",
    },
    "C": {
        "X": "Y",
        "Y": "Z",
        "Z": "X",
    },
}


def score_for_round(theirs, mine):
    score = 0
    score += my_score[mine]
    score += battle_result[theirs][mine]
    return score

def total_score(plan):
    return sum(score_for_round(*row.split()) for row in plan)

def score_to_result(theirs, target):
    score = 0
    mine = choose_throw[theirs][target]
    score += my_score[mine]
    score += score_for_result[target]
    return score

def total_score_to_result(plan):
    return sum(score_to_result(*row.split()) for row in plan)

def test_cases():
    verify(score_for_round("A", "Y"), 8)
    verify(score_for_round("B", "X"), 1)
    verify(score_for_round("C", "Z"), 6)
    verify(total_score(example_plan), 15)
    verify(score_to_result("A", "Y"), 4)
    verify(score_to_result("B", "X"), 1)
    verify(score_to_result("C", "Z"), 7)
    verify(total_score_to_result(example_plan), 12)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())