#!/usr/bin/env python3

import unittest

class Test(unittest.TestCase):
    def test_run(self):
        assert True

    def test_result(self):
        assert Elf().execute() == 0

class Elf():
    def execute(self) -> int:
        with open('input/day.0.txt') as inp:
            lines = inp.readlines()
        data = [l.strip() for l in lines if len(l.strip()) > 0]
        return len(data)

if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())