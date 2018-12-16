#!/usr/bin/env python3

import time

def execute():
    return highest_power_cordinate(1133)

def energy_level(x, y, serial_number):
    rack_id = x + 10
    result = ((rack_id * y) + serial_number) * rack_id
    hundreds_digit = (result // 100) % 10
    return hundreds_digit - 5
    
def highest_power_cordinate(serial_number):
    grid_size = 300
    grid = [[None] * grid_size for i in range(grid_size)]
    max_power = None
    max_x = -1
    max_y = -1
    max_window_size = -1
    
    for x in range(grid_size):
        for y in range(grid_size):
            grid[x][y] = energy_level(x, y, serial_number)
            
    last_t = time.time()
    energy_grid = {}
    for w in range(2,grid_size):
        energy_grid[w] = [[None] * (grid_size-w) for i in range(grid_size-w)]
        factor = None
        if w > 2:
            for f in range(2,w):
                if (w / f) in energy_grid:
                    # factor = f
                    break

        for x in range(grid_size - w):
            for y in range(grid_size - w):
                if factor is not None:
                    energy = sum([sum(energy_grid[w / factor][x+c][y:y+factor+1]) for c in range(factor)])
                elif w > 3:
                    energy = energy_grid[w-1][x][y] + energy_grid[w-1][x+1][y+1] + grid[x][y+w-1] + grid[x+w-1][y] - energy_grid[w-2][x+1][y+1]
                else:
                    energy = sum([sum(grid[x+c][y:y+w]) for c in range(w)])
                if max_power is None or energy > max_power:
                    max_power = energy
                    max_x = x
                    max_y = y
                    max_window_size = w
                energy_grid[w][x][y] = energy
#            print('.', end='')
        t = time.time()
        print(':', w, '-', t - last_t, 'factor =', factor, (max_x, max_y, max_window_size, max_power))
        last_t = t
    return (max_x, max_y, max_window_size)

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

#Fuel cell at  122,79, grid serial number 57: power level -5.
#Fuel cell at 217,196, grid serial number 39: power level  0.
#Fuel cell at 101,153, grid serial number 71: power level  4.

def test_cases():
    verify(energy_level(3, 5, 8), 4)
    verify(energy_level(122, 79, 57), -5)
    verify(energy_level(217, 196, 39), 0)
    verify(energy_level(101, 153, 71), 4)

    verify(highest_power_cordinate(18), (90,269,16))
    verify(highest_power_cordinate(42), (232,251,12))

if __name__ == "__main__":
    test_cases()
    print(execute())