#!/usr/bin/env python3

import unittest
import typing
from parameterized import parameterized
import math

class Test(unittest.TestCase):
    data = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   + """.splitlines()

    def test_run(self):
        self.assertTrue(True)

    def test_result(self):
        self.assertEqual(0, Elf().execute())

    def test_data(self):
        self.assertEqual(4277556, Elf().solve(self.data))

    @parameterized.expand([
        [33210, ["123", "45", "6", "*"]],
        [490, ["328", "64", "98", "+"]],
    ])
    def test_examples(self, expected, input):
        self.assertEqual(expected, Elf().calculate(input))

class Elf():
    def open_file(self) -> list[str]:
        with open('2025/input/day.6.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())

    def solve(self, data: list[str]) -> int:
        equations = list(zip(*(line.split() for line in data)))
        return sum(self.calculate(list(eq)) for eq in equations)

    def calculate(self, items: list[str]) -> int:
        total = 0
        if items[-1] == '*':
            total = math.prod(int(x) for x in items[:-1])
        elif items[-1] == '+':
            total = sum(int(x) for x in items[:-1])
        return total

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())