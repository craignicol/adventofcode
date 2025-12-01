#!/usr/bin/env python3

import unittest
import typing

class Test(unittest.TestCase):
    data = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82""".splitlines()

    def test_run(self):
        self.assertTrue(True)

    def test_result(self):
        self.assertEqual(0, Elf().execute())

    def test_data(self):
        self.assertEqual(0, Elf().solve([]))
        self.assertEqual(3, Elf().solve(self.data))

class Elf():
    def open_file(self) -> list[str]:
        with open('2025/input/day.1.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())

    def solve(self, data: list[str]) -> int:
        arrow_pos = 50
        zero_count = 0
        for step in data:
            if step[0] == "L":
                arrow_pos = (arrow_pos - int(step[1:])) % 100
            elif step[0] == "R":
                arrow_pos = (arrow_pos + int(step[1:])) % 100
            if arrow_pos == 0:
                zero_count += 1
        return zero_count

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())