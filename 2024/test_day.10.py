#!/usr/bin/env python3

from collections import defaultdict
import unittest
import typing

class Test(unittest.TestCase):
    data = """0123
1234
8765
9876""".splitlines()
    
    data2 = """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9""".splitlines()

    data3 = """..90..9
...1.98
...2..7
6543456
765.987
876....
987....""".splitlines()

    data4 = """10..9..
2...8..
3...7..
4567654
...8..3
...9..2
.....01""".splitlines()

    data5 = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".splitlines()

    def test_run(self):
        self.assertTrue(True)

    def test_result(self):
        self.assertEqual(0, Elf().execute())

    def test_data(self):
        self.assertEqual(1, Elf().solve(self.data))
        self.assertEqual(2, Elf().solve(self.data2))
        self.assertEqual(4, Elf().solve(self.data3))
        self.assertEqual(3, Elf().solve(self.data4))
        self.assertEqual(36, Elf().solve(self.data5))

class Elf():
    def open_file(self) -> list[str]:
        with open('2024/input/day.10.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())

    def solve(self, data: list[str]) -> int:
        elevations = self.parse(data)
        trailheads = list(elevations['0'])
        results = []

        for t in trailheads:
            results.extend(self.score(t, elevations))

        return len(results)

    def score(self, start: tuple[int,int], elevations: dict[set[tuple[int,int]]]) -> set[tuple[int,int]]:
        directions = [(-1,0),(0,1),(1,0),(0,-1)]
        trailheads = set([start])
        for next in '123456789':
            up = set()
            for t in trailheads:
                for d in directions:
                    step = (t[0] + d[0], t[1] + d[1])
                    if step in elevations[next]:
                        up.add(step)
            trailheads = up
        return trailheads

    def parse(self, data: list[str]) -> dict[set[tuple[int,int]]]:
        elevations = defaultdict(set)
        for i in range(len(data)):
            for j in range(len(data[i])):
                elevations[data[i][j]].add((i,j))
        return elevations

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())