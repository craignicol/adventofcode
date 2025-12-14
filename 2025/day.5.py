#!/usr/bin/env python3

import unittest
import typing
from parameterized import parameterized

class Test(unittest.TestCase):
    data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32""".splitlines()

    def test_run(self):
        self.assertTrue(True)

    def test_result(self):
        self.assertEqual(0, Elf().execute())

    def test_data(self):
        self.assertEqual(3, Elf().solve(self.data))

    @parameterized.expand([
        [0, []],
    ])
    def test_examples(self, expected, input):
        self.assertEqual(expected, Elf().solve(input))

class Elf():
    def open_file(self) -> list[str]:
        with open('2025/input/day.5.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())

    def solve(self, data: list[str]) -> int:
        ranges = []
        numbers = []
        for line in data:
            if '-' in line:
                start, end = map(int, line.split('-'))
                ranges.append((start, end))
            elif len(line) > 0:
                numbers.append(int(line))

        count = 0
        for num in numbers:
            for start, end in ranges:
                if start <= num <= end:
                    count += 1
                    break

        return count

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())