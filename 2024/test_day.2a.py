#!/usr/bin/env python3

import unittest
import typing

## with dampening

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
        self.assertEqual(4, Elf().solve(self.data))

    def test_is_safe(self):
        self.assertEqual(True, Elf().is_safe(self.data[0]))
        self.assertEqual(True, Elf().is_safe(self.data[3]))
        self.assertEqual(True, Elf().is_safe(self.data[4]))
        self.assertEqual(True, Elf().is_safe(self.data[5]))

        self.assertEqual(True, Elf().is_safe("4 4 5 6 7 10"))
        self.assertEqual(True, Elf().is_safe("10 8 8 7 6 4"))
        self.assertEqual(True, Elf().is_safe("10 8 7 6 4 4"))
        self.assertEqual(True, Elf().is_safe("8 10 8 7 6 4"))
        self.assertEqual(True, Elf().is_safe("8 12 7 6 4 3 1"))

    def test_is_not_safe(self):
        self.assertEqual(False, Elf().is_safe(self.data[1]))
        self.assertEqual(False, Elf().is_safe(self.data[2]))

class Elf():
    def open_file(self) -> list[str]:
        with open('2024/input/day.2.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())

    def is_safe(self, report: str, dampened: bool = False) -> bool:
        levels = [int(l) for l in report.split()]
        direction = +1 if levels[1] - levels[0] > 0 else -1
        i = 1
        while i < (len(levels)):
            diff = (levels[i] - levels[i-1]) * direction
            if diff < 1 or diff > 3:
                if dampened:
                    return False
                if i == len(levels) - 1:
                    return True
                diff = (levels[i+1] - levels[i-1]) * direction # skip i
                if diff < 1 or diff > 3:
                    return self.is_safe(' '.join([str(l) for l in levels[1:]]), True) or \
                           self.is_safe(' '.join([str(levels[0])] +[str(l) for l in levels[2:]]), True)
                dampened = True
                i += 1
            i += 1
        return True

    def solve(self, data: list[str]) -> int:
        return len([r for r in data if self.is_safe(r)])

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())