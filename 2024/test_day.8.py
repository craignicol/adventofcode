#!/usr/bin/env python3

from collections import defaultdict
import unittest
import typing

class Test(unittest.TestCase):
    data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".splitlines()

    def test_run(self):
        self.assertTrue(True)

    def test_result(self):
        self.assertEqual(0, Elf().execute())

    def test_result_b(self):
        self.assertEqual(0, Elf(50).execute())

    def test_data(self):
        self.assertEqual(14, Elf().solve(self.data))
        self.assertEqual(34, Elf(50).solve(self.data))

class Elf():
    def __init__(self, max: int = 1):
        self.max = max
        self.min = 1 if max == 1 else 0

    def open_file(self) -> list[str]:
        with open('2024/input/day.8.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())

    def solve(self, data: list[str]) -> int:
        antennas = self.parse(data)
        return len(self.generate_antenodes(antennas))

    def parse(self, data: list[str]) -> dict[list[tuple[int,int]]]:
        self.bounds = len(data), len(data[0])
        antennas = defaultdict(list)
        for i in range(self.bounds[0]):
            for j in range(self.bounds[1]):
                if data[i][j] != '.':
                    antennas[data[i][j]].append((i,j))
        return antennas

    def generate_antenodes(self, antennas: dict[list[tuple[int,int]]]) -> set[tuple[int,int]]:
        antenodes = set()
        for f in antennas:
            a = antennas[f]
            if len(a) < 2:
                continue
            antenodes.update([an for an in self.find_antenodes(a) if self.in_bounds(an)])
        return antenodes
    
    def find_antenodes(self, antenna: list[tuple[int,int]]) -> set[tuple[int,int]]:
        antenodes = set()
        for i, x in enumerate(antenna):
            if i == len(antenna) - 1:
                break
            for y in antenna[i+1:]:
                diff = (y[0] - x[0], y[1] - x[1])
                for m in range(self.min, self.max + 1): # 0 to also include antenna positions
                    antenodes.add((y[0] + m * diff[0], y[1] + m * diff[1]))
                    antenodes.add((x[0] - m * diff[0], x[1] - m * diff[1]))
        return antenodes
                
    def in_bounds(self, a: tuple[int,int]) -> bool:
        if a[0] < 0 or a[0] >= self.bounds[0] or a[1] < 0 or a[1] >= self.bounds[1]:
            return False
        return True


if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())