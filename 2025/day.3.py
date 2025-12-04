#!/usr/bin/env python3

import unittest
import typing
from parameterized import parameterized

class Test(unittest.TestCase):
    data = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()

    def test_run(self):
        self.assertTrue(True)

    def test_result(self):
        self.assertEqual(0, Elf().execute())

    def test_data(self):
        self.assertEqual(357, Elf().solve(self.data))

    @parameterized.expand([
        [98, ["987654321111111"]],
        [89, ["811111111111119"]],
        [78, ["234234234234278"]],
        [92, ["818181911112111"]]
    ])
    def test_examples(self, expected, input):
        self.assertEqual(expected, Elf().solve(input))

class Elf():
    def open_file(self) -> list[str]:
        with open('2025/input/day.3.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())

    def max_joltage(self, batteries: str) -> int:
        # Need to leave space for 2nd digit
        first, first_idx = max(batteries[:-1]), batteries.index(max(batteries[:-1]))
        second = max(batteries[(first_idx+1):])
        return int(first + second)

    def solve(self, data: list[str]) -> int:
        return sum([self.max_joltage(b) for b in data])

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())