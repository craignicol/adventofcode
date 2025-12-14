#!/usr/bin/env python3

import unittest
import typing
from parameterized import parameterized

class Test(unittest.TestCase):
    data = """3-5
10-14
16-20
12-18

1
5
8
11
17
32""".splitlines()

    def test_run(self):
        self.assertTrue(True)

    def test_result(self):
        self.assertEqual((0, 0), Elf().execute())

    def test_data(self):
        self.assertEqual((3, 14), Elf().solve(self.data))

class Elf():
    def open_file(self) -> list[str]:
        with open('2025/input/day.5.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> (int, int):
        return self.solve(self.open_file())

    def solve(self, data: list[str]) -> (int, int):
        ranges = []
        numbers = []
        for line in data:
            if '-' in line:
                start, end = map(int, line.split('-'))
                ranges.append((start, end))
            elif len(line) > 0:
                numbers.append(int(line))

        sorted_ranges = sorted(ranges, key=lambda x: x[0])
        merged_ranges = []
        for current in sorted_ranges:
            if not merged_ranges:
                merged_ranges.append(current)
            else:
                last_start, last_end = merged_ranges[-1]
                current_start, current_end = current
                if current_start <= last_end + 1:
                    merged_ranges[-1] = (last_start, max(last_end, current_end))
                else:
                    merged_ranges.append(current)
        fresh_count = sum([end - start + 1 for start, end in merged_ranges])

        count = 0
        for num in numbers:
            for start, end in ranges:
                if start <= num <= end:
                    count += 1
                    break

        return (count, fresh_count)

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())