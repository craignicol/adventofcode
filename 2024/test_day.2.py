#!/usr/bin/env python3

import unittest
import typing

class Test(unittest.TestCase):
    data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".splitlines()

    def test_run(self):
        self.assertTrue(True)

    def test_result(self):
        self.assertEqual(0, Elf().execute())

    def test_count_safe(self):
        self.assertEqual(2, Elf().solve(self.data))

    def test_is_safe(self):
        self.assertEqual(True, Elf().is_safe(self.data[0]))

    def test_is_not_safe(self):
        self.assertEqual(False, Elf().is_safe(self.data[1]))

class Elf():
    def open_file(self) -> list[str]:
        with open('2024/input/day.2.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())

    def is_safe(self, report: str) -> bool:
        levels = [int(l) for l in report.split()]
        if levels[0] == levels[1]:
            return False
        direction = +1 if levels[1] - levels[0] > 0 else -1
        for i in range(1,len(levels)):
            diff = (levels[i] - levels[i-1]) * direction
            if diff < 1 or diff > 3:
                return False
        return True

    def solve(self, data: list[str]) -> int:
        for r in data:
            print(self.is_safe(r), '-', r)
        return len([r for r in data if self.is_safe(r)])

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())