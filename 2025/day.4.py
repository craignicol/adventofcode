#!/usr/bin/env python3

import unittest
import typing
from parameterized import parameterized

class Test(unittest.TestCase):
    data = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.""".splitlines()

    def test_run(self):
        self.assertTrue(True)

    def test_result(self):
        self.assertEqual(0, Elf().execute())

    def test_data(self):
        self.assertEqual(13, Elf().solve(self.data))

    @parameterized.expand([
        [0, []],
    ])
    def test_examples(self, expected, input):
        self.assertEqual(expected, Elf().solve(input))

class Elf():
    def open_file(self) -> list[str]:
        with open('2025/input/day.4.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())

    def solve(self, data: list[str]) -> int:
        counts:list[list[int]] = [[0 for _ in range(len(data[0]))] for _ in range(len(data))]
        for y in range(len(data)):
            row = data[y]
            for x in range(len(row)):
                if row[x] == '@':
                    for dy in [-1, 0, 1]:
                        for dx in [-1, 0, 1]:
                            if dy == 0 and dx == 0:
                                continue
                            ny, nx = y+dy, x+dx
                            if 0 <= ny < len(data) and 0 <= nx < len(row):
                                counts[ny][nx] += 1
        print(counts)
        return sum(1 for y in range(len(data)) for x in range(len(data[0])) if counts[y][x] < 4 and data[y][x] == '@')                

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())