#!/usr/bin/env python3

import unittest
import typing

class Test(unittest.TestCase):
    data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".splitlines()

    def test_run(self):
        self.assertTrue(True)

    def test_result(self):
        self.assertEqual(0, Elf().execute())

    def test_result_b(self):
        self.assertEqual(0, Elf().execute_fix())

    def test_example_data(self):
        self.assertEqual(143, Elf().solve(self.data))
        self.assertEqual(123, Elf().fix(self.data))

    def test_update_per_page(self):
        sut = Print(self.data)

        self.assertEqual(True, sut.check_update(0))
        self.assertEqual(True, sut.check_update(1))
        self.assertEqual(True, sut.check_update(2))
        self.assertEqual(False, sut.check_update(3))
        self.assertEqual(False, sut.check_update(4))
        self.assertEqual(False, sut.check_update(5))


class Elf():
    def open_file(self) -> list[str]:
        with open('2024/input/day.5.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())

    def execute_fix(self) -> int:
        return self.fix(self.open_file())

    def solve(self, data: list[str]) -> int:
        return Print(data).score_all_updates()

    def fix(self, data: list[str]) -> int:
        return Print(data).fix()
    
class Print():
    rules: set[tuple[int,int]]
    pages: list[list[int]]

    def __init__(self, data: list[str]) -> None:
        self.parse(data)

    def __repr__(self) -> str:
        return 'Print:\n' + str(self.rules) + '\n' + str(self.pages)

    def parse(self, data: list[str]) -> None:
        self.rules = set()
        self.pages = []
        for d in data:
            r = d.split('|')
            if len(r) == 2:
                self.rules.add(tuple([int(p) for p in r]))
                continue
            p = d.split(',')
            if len(p) > 1:
                self.pages.append([int(n) for n in p])

    def check_update(self, update: int) -> bool:
        return self.valid_update(self.pages[update])

    def valid_update(self, pages: list[int]) -> bool:
        for i, p in enumerate(pages):
            for q in pages[i+1:]:
                if (q,p) in self.rules:
                    return False
        return True

    def score_all_updates(self) -> int:
        valid_updates = [p for p in self.pages if self.valid_update(p)]
        middle_pages = [p[len(p)//2] for p in valid_updates]
        return sum(middle_pages)

    def fix_update(self, pages: list[int]) -> list[int]:
        updated = pages[:]
        while not self.valid_update(updated):
            for i in range(len(pages)):
                for j in range(i+1, len(pages)):
                    p = updated[i]
                    q = updated[j]
                    if (q,p) in self.rules:
                        updated[i] = q
                        updated[j] = p
                        break
        return updated

    def fix(self) -> int:
        invalid_updates = [p for p in self.pages if not self.valid_update(p)]
        valid_updates = [self.fix_update(p) for p in invalid_updates]
        middle_pages = [p[len(p)//2] for p in valid_updates]
        return sum(middle_pages)

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())