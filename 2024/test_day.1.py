#!/usr/bin/env python3

import unittest
import typing

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

    def test_result(self):
        self.assertEqual(0, Elf().execute())

class Elf():
    def open_file(self) -> list[str]:
        with open('2024/input/day.1.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())

    def solve(self, data: list[str]) -> int:
        if len(data) < 1:
            return 0
        pairs = [tuple([int(n) for n in d.split()]) for d in data]
        l1, l2 = [sorted(list(p)) for p in zip(*pairs)]
        return sum([abs(z[0] - z[1]) for z in zip(l1, l2)])

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())