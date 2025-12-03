#!/usr/bin/env python3

import unittest
import typing
from parameterized import parameterized
import itertools

class Test(unittest.TestCase):
    data = """""".splitlines()

    def test_run(self):
        self.assertTrue(True)

    def test_result(self):
        self.assertEqual(0, Elf().execute())

    def test_data(self):
        self.assertEqual(0, Elf().solve(self.data))

    @parameterized.expand([
        [1227775554, ["11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"]],
    ])
    def test_examples(self, expected, input):
        self.assertEqual(expected, Elf().solve(input))

    @parameterized.expand([
        [[], "1-9"],
        [[11, 22], "11-22"],
        [[99], "95-115"],
        [[1010], "998-1012"],
        [[1188511885], "1188511880-1188511890"],
        [[222222], "222220-222224"],
        [[], "1698522-1698528"],
        [[446446], "446443-446449"],
        [[38593859],"38593856-38593862"],
        [[],"565653-565659"],
        [[], "824824821-824824827"],
        [[], "2121212118-2121212124"]
    ])
    def test_list_invalid(self, expected: list[str], input: str):
        self.assertEqual(expected, Elf().list_invalid(input), input)

class Elf():
    def open_file(self) -> list[str]:
        with open('2025/input/day.2.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())

    def list_invalid(self, id_range: str) -> list[int]:
        invalid = []
        [low, high] = id_range.split("-")
        start = int(low[:max(1,len(low)//2)])
        end = int(high[:max(1,len(high)//2)])
        if end < start:
            end *= 10

        # print((start, end), id_range)

        [low, high] = [int(low), int(high)]
        
        for i in range(start, end+1):
            next = int(str(i) + str(i))
            if low <= next and next <= high:
                invalid.append(next)

        return invalid

    def solve(self, data: list[str]) -> int:
        invalid = []
        data = itertools.chain(*[d.split(",") for d in data])
        for d in data:
            invalid += self.list_invalid(d)
        return sum(invalid)

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())