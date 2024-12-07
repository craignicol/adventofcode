#!/usr/bin/env python3

import unittest
import typing

class Test(unittest.TestCase):
    data = """""".splitlines()

    def test_run(self):
        self.assertTrue(True)

    def test_result(self):
        self.assertEqual(0, Elf().execute())

    def test_data(self):
        self.assertEqual(0, Elf().solve(self.data))

class Elf():
    def open_file(self) -> list[str]:
        with open('2024/input/day.0.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())

    def solve(self, data: list[str]) -> int:
        return len(data)

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())