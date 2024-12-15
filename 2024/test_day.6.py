#!/usr/bin/env python3

import unittest
import typing

class Test(unittest.TestCase):
    data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()

    def test_run(self):
        self.assertTrue(True)

    def test_result(self):
        self.assertLess(Elf().execute(), 5445)
        self.assertEqual(0, Elf().execute())
        self.assertEqual(0, Elf().execute_obstacles())

    def test_data(self):
        self.assertEqual(41, Elf().solve(self.data))

    def test_data(self):
        self.assertEqual(6, Elf().solve_obstacles(self.data))

class Elf():
    def open_file(self) -> list[str]:
        with open('2024/input/day.6.txt') as inp:
            lines = inp.readlines()
        return [l.strip() for l in lines if len(l.strip()) > 0]

    def execute(self) -> int:
        return self.solve(self.open_file())
    
    def execute_obstacles(self) -> int:
        return self.solve_obstacles(self.open_file())

    def solve(self, data: list[str]) -> int:
        return Map(data).steps_to_exit()
    
    def solve_obstacles(self, data: list[str]) -> int:
        return Map(data).place_obstacles()

class Map():
    directions: list[tuple[int,int]] = [(-1,0),(0,1), (1,0), (0,-1)] # up, right, down, left

    def __init__(self, data: list[str]):
        self.bounds: tuple[int,int,int,int] = (0,0,0,0)
        self.obstacles: set[tuple[int,int]] = set()
        self.start: tuple[int,int] = (0,0)
        self.path_taken = set()
        self.crossovers = 0
        self.parse(data)

    def __repr__(self) -> str:
        for i in range(self.bounds[0], self.bounds[1]):
            for j in range(self.bounds[2], self.bounds[3]):
                if (i,j) in self.obstacles:
                    print('#', end='')
                elif (i,j) == self.start:
                    print('^', end='')
                elif (i,j) in self.path_taken:
                    print('X', end='')
                else:
                    print('.', end='')
            print()
        return ''

    def parse(self, data: list[str]):
        for i, r in enumerate(data):
            for j, c in enumerate(r):
                if c == '#':
                    self.obstacles.add((i,j))
                elif c == '^':
                    self.start = (i,j)
        self.bounds = (0, len(data), 0, len(data[0]))

    def steps_to_exit(self) -> int:
        position = self.start
        direction = 0
        while position[0] >= self.bounds[0] and position[0] < self.bounds[1] and position[1] >= self.bounds[2] and position[1] < self.bounds[3]:
            next = self.next_position(position, direction)
            if next in self.obstacles:
                direction = (direction + 1) % len(self.directions) #turn right
            else:
                if next in self.path_taken:
                    self.crossovers += 1
                self.path_taken.add(position)
                position = next #move forward
        return len(self.path_taken)

    def next_position(self, position: tuple[int,int], direction: int) -> tuple[int,int]:
        d = self.directions[direction]
        return (position[0] + d[0], position[1] + d[1])

    def place_obstacles(self) -> int:
        self.steps_to_exit()
        return self.crossovers
        
if __name__ == "__main__":
    unittest.main()
    print(Elf().execute())