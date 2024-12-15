#!/usr/bin/env python3

import unittest
import typing

class Test(unittest.TestCase):
    data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".splitlines()

    def test_run(self):
        self.assertTrue(True)

    def test_result(self):
        self.assertEqual(0, Elf().execute())

    def test_data(self):
        self.assertEqual(3749, Elf().solve(self.data))

    def test_is_possible(self):
        expected = [True, True, False, False, False, False, False, False, True]

        for i in range(0, len(self.data)):
            with self.subTest(i=i):
                self.assertEqual(expected[i], Elf().is_possible(self.data[i]) > 0)

class Elf():
    def open_file(self) -> list[str]:
        with open('2024/input/day.7.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())

    def solve(self, data: list[str]) -> int:
        return sum([self.is_possible(d) for d in data])

    def is_possible(self, data: str) -> bool:
        target, values = data.split(':')
        target = int(target)
        values = [int(v) for v in values.split()]
        results = [values[0]]
        for v in values[1:]:
            next = []
            for r in results:
                next.append(r + v)
                next.append(r * v)
            results = next
        return target if target in results else 0
    
if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())