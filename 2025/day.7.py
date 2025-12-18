#!/usr/bin/env python3

import unittest
import typing
from parameterized import parameterized

class Test(unittest.TestCase):
    data = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............""".splitlines()

    def test_run(self):
        self.assertTrue(True)

    def test_result(self):
        self.assertEqual(0, Elf().execute())

    def test_data(self):
        self.assertEqual(21, Elf().solve(self.data))

    @parameterized.expand([
        [1, [".S.", "...", ".^.", "...", "..."]],
        [3, ["..S..", ".....", "..^..", ".....", ".^.^.","....."]],
    ])
    def test_examples(self, expected, input):
        self.assertEqual(expected, Elf().solve(input))

class Elf():
    def open_file(self) -> list[str]:
        with open('2025/input/day.7.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())

    def solve(self, data: list[str]) -> int:
        splits = 0
        next_line = "." * len(data[0])
        for line in data:
            for i, c in enumerate(line):
                if c in "|S":
                    next_line = next_line[:i] + "|" + next_line[i+1:]
                elif c == "^":
                    if next_line[i] == "|":
                        next_line = next_line[:i-1] + "|.|" + next_line[i+2:]
                        splits += 1
                    else:
                        next_line = next_line[:i] + "." + next_line[i+1:]
        return splits

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())