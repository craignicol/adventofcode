#!/usr/bin/env python3

import unittest
import typing

class Test(unittest.TestCase):
    data1 = """M.S
.A.
M.S""".splitlines()

    data2 = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()

    def test_run(self):
        self.assertTrue(True)

    def test_result(self):
        self.assertEqual(0, Elf().execute())

    def test_data1(self):
        self.assertEqual(1, Elf().solve(self.data1))

    def test_data2(self):
        self.assertEqual(9, Elf().solve(self.data2))

class Elf():
    def open_file(self) -> list[str]:
        with open('2024/input/day.4.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())

    def solve(self, data: list[str]) -> int:
        xmas_count = 0
        for i in range(1, len(data)-1):
            for j in range(1, len(data[i])-1):
                if data[i][j] == 'A':
                    xmas_count += self.count_xmas(data, i, j)
        return xmas_count

    def count_xmas(self, data: list[str], i: int, j: int) -> int:
        count = 0
        directions = [(-1,-1), (-1,1), (1,-1), (1,1)]
        values = [data[i+d[0]][j+d[1]] for d in directions]
        [d1a, d2a, d2b, d1b] = values 
        if d1a == 'M' and d1b == 'S':
            count += 1
        if d1a == 'S' and d1b == 'M':
            count += 1
        if d2a == 'M' and d2b == 'S':
            count += 1
        if d2a == 'S' and d2b == 'M':
            count += 1
        # print(values, count)
        return count // 2 # has to be both directions

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())