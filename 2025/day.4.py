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

    def test_repeat(self):
        self.assertEqual(43, Elf().solve(self.data, repeat=True))

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
        return self.solve(self.open_file(), repeat=True)

    def solve(self, data: list[str], repeat: bool = False) -> int:
        if repeat:
            total = 0
            (new_total, data) = self.remove_one(data)
            while new_total > 0:
                total += new_total
                (new_total, data) = self.remove_one(data)
            return total
        return self.remove_one(data)[0]

    def remove_one(self, data: list[str]) -> (int, list[str]):
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
        num_to_remove = sum(1 for y in range(len(data)) for x in range(len(data[0])) if counts[y][x] < 4 and data[y][x] == '@')                
        return (num_to_remove, [''.join(['.' if counts[y][x] < 4 and data[y][x] == '@' else data[y][x] for x in range(len(data[0]))]) for y in range(len(data))])

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())