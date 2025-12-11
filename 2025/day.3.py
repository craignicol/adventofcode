#!/usr/bin/env python3

import unittest
import typing
from parameterized import parameterized

class Test(unittest.TestCase):
    data = """987654321111111
811111111111119
234234234234278
818181911112111""".splitlines()

    def test_run(self):
        self.assertTrue(True)

    def test_result(self):
        self.assertEqual(0, Elf().execute(12))

    def test_data(self):
        self.assertEqual(357, Elf().solve(self.data))
        self.assertEqual(3121910778619, Elf().solve(self.data, 12))

    @parameterized.expand([
        [98, ["987654321111111"]],
        [89, ["811111111111119"]],
        [78, ["234234234234278"]],
        [92, ["818181911112111"]]
    ])
    def test_examples(self, expected, input):
        self.assertEqual(expected, Elf().solve(input))

    @parameterized.expand([
        [987654321111, ["987654321111111"]],
        [811111111119, ["811111111111119"]],
        [434234234278, ["234234234234278"]],
        [888911112111, ["818181911112111"]]
    ])
    def test_examples(self, expected, input):
        self.assertEqual(expected, Elf().solve(input, 12))

class Elf():
    def open_file(self) -> list[str]:
        with open('2025/input/day.3.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self, window: int) -> int:
        return self.solve(self.open_file(), window)

    def max_joltage(self, batteries: str, window: int = 2) -> int:
        # Need to leave space for nth digit
        if len(batteries) < window:
            return 0
        largest = ""
        last_idx = 0
        for n in range(window-1, 0, -1):
            nxt, nxt_idx = max(batteries[:-n]), batteries.index(max(batteries[:-n]))
            largest += nxt
            #last_idx = nxt_idx+max(1,last_idx)
            batteries = batteries[nxt_idx+1:]
        largest += max(batteries)
        return int(largest)

    def solve(self, data: list[str], window: int = 2) -> int:
        return sum([self.max_joltage(b, window) for b in data])

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())