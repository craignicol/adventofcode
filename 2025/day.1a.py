#!/usr/bin/env python3

import unittest
import typing
from parameterized import parameterized

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

    @parameterized.expand([
        [0, []],
        [10, ["R1000"]],
        [10, ["L1000"]],
        [1, ["L75", "R20"]],
        [1, ["R75", "L20"]],
        [1, ["L50", "R50"]],
        [1, ["L50", "L50"]],
        [1, ["R50", "R50"]],
        [1, ["R50", "L50"]],
        [2, ["L200"]],
        [2, ["R200"]],
        [2, ["L150", "L50"]],
        [2, ["L150", "R50"]],
        [2, ["R150", "L50"]],
        [2, ["R150", "R50"]]
    ])
    def test_examples(self, expected, input):
        self.assertEqual(expected, Elf().solve(input), msg=input)

    def test_data(self):
        self.assertEqual(6, Elf().solve(self.data))

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
        ignore_next = False
        for step in data:
            if step[0] == "L":
                arrow_pos -= int(step[1:])
                if ignore_next:
                    ignore_next = False
                    if arrow_pos < 0:
                        arrow_pos += 100
                while arrow_pos < 0:
                    arrow_pos += 100
                    zero_count += 1
                if arrow_pos == 0:                       
                    zero_count += 1
                    ignore_next = True
            elif step[0] == "R":
                arrow_pos += int(step[1:])
                if ignore_next:
                    ignore_next = False
                    if arrow_pos >= 100:
                        arrow_pos -= 100
                while arrow_pos >= 100:
                    arrow_pos -= 100
                    zero_count += 1
                if arrow_pos == 0:
                    ignore_next = True
        return zero_count

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())