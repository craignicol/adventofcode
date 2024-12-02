#!/usr/bin/env python3

import unittest
from collections import defaultdict

class Test(unittest.TestCase):
    data1 = """3   4
4   3
2   5
1   3
3   9
3   3""".splitlines()

    data_single = "1   3".splitlines()

    def test_run(self):
        self.assertTrue(True)

    def test_given_example(self):
        self.assertEqual(11, Elf().solve(self.data1))

    def test_single(self):
        self.assertEqual(2, Elf().solve(self.data_single))

    def test_similarity_example(self):
        self.assertEqual(31, Elf().similarity(self.data1))

    def test_similarity_single(self):
        self.assertEqual(0, Elf().similarity(self.data_single))

    def test_result_a(self):
        self.assertEqual(0, Elf().execute())

    def test_result_b(self):
        self.assertEqual(0, Elf().execute_similarity())

class Elf():
    def open_file(self) -> list[str]:
        with open('2024/input/day.1.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())

    def execute_similarity(self) -> int:
        return self.similarity(self.open_file())

    def frequency(self, data: list[int]) -> dict[int,int]:
        freq = defaultdict(int)
        for d in data:
            freq[d] += 1
        return freq

    def similarity(self, data: list[str]) -> int:
        if len(data) < 1:
            return 0
        pairs = [tuple([int(n) for n in d.split()]) for d in data]
        l1, l2 = [list(p) for p in zip(*pairs)]
        f2 = self.frequency(l2)
        return sum([i * f2[i] for i in l1])

    def solve(self, data: list[str]) -> int:
        if len(data) < 1:
            return 0
        pairs = [tuple([int(n) for n in d.split()]) for d in data]
        l1, l2 = [sorted(list(p)) for p in zip(*pairs)]
        return sum([abs(z[0] - z[1]) for z in zip(l1, l2)])

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())