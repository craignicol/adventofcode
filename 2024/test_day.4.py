#!/usr/bin/env python3

import unittest
import typing

class Test(unittest.TestCase):
    data1 = """..X...
.SAMX.
.A..A.
XMAS.S
.X....""".splitlines()

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
        self.assertEqual(4, Elf().solve(self.data1))

    def test_data2(self):
        self.assertEqual(18, Elf().solve(self.data2))

class Elf():
    def open_file(self) -> list[str]:
        with open('2024/input/day.4.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())

    def solve(self, data: list[str]) -> int:
        xmas_count = 0
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == 'X':
                    xmas_count += self.count_xmas(data, i, j)
        return xmas_count

    def count_xmas(self, data: list[str], i: int, j: int) -> int:
        count = 0
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for d in directions:
            if i+3*d[0] < 0 or i+3*d[0] >= len(data) or j+3*d[1] < 0 or j+3*d[1] >= len(data[i]):
                continue
            if data[i+d[0]][j+d[1]] == 'M' and data[i+2*d[0]][j+2*d[1]] == 'A' and data[i+3*d[0]][j+3*d[1]] == 'S':
                count += 1
        return count

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())