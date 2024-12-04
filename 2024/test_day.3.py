#!/usr/bin/env python3

import unittest
import re

class Test(unittest.TestCase):
    data = """xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"""
    datab = """xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"""

    def test_run(self):
        self.assertTrue(True)

    def test_result(self):
        self.assertEqual(0, Elf().execute())

    def test_sample(self):
        self.assertEqual(161, Elf().solve(self.data))

    def test_result(self):
        self.assertEqual(0, ElfDoDont().execute())

    def test_sample(self):
        self.assertEqual(48, ElfDoDont().solve(self.datab))


class Elf():
    def open_file(self) -> str:
        with open('2024/input/day.3.txt') as inp:
            lines = inp.read()
        return lines.strip()

    def execute(self) -> int:
        return self.solve(self.open_file())

    # find all occurences of `mul(\d+,\d+)` in the string as capture groups
    def find_mul(self, data: str) -> list[tuple[int,int]]:
        return [(int(m.group(1)), int(m.group(2))) for m in re.finditer(r'mul\((\d+),(\d+)\)', data, re.MULTILINE | re.DOTALL)]

    def solve(self, data: str) -> int:
        pairs = self.find_mul(data)
        return sum([p[0] * p[1] for p in pairs])

class ElfDoDont():
    def open_file(self) -> str:
        with open('2024/input/day.3.txt') as inp:
            lines = inp.read()
        return lines.strip()

    def execute(self) -> int:
        return self.solve(self.open_file())

    # find all occurences of `mul(\d+,\d+)` in the string as capture groups
    def find_mul(self, data: str) -> list[tuple[int,int]]:
        return [(int(m.group(1)), int(m.group(2))) for m in re.finditer(r'mul\((\d+),(\d+)\)', data, re.MULTILINE | re.DOTALL)]

    def solve(self, data: str) -> int:
        # split the string into groups with `do()` and `don't()` separators
        split_data = [d.split('don\'t()')[0] for d in data.split('do()')]

        pairs = self.find_mul(''.join(split_data))
        return sum([p[0] * p[1] for p in pairs])

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())