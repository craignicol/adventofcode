#!/usr/bin/env python3

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
    for x in range(grid_size):
        for y in range(grid_size):
            grid[x][y] = energy_level(x, y, serial_number)
    for x in range(grid_size-2):
        for y in range(grid_size-2):
            energy = sum(grid[x][y:y+3]) + sum(grid[x+1][y:y+3]) + sum(grid[x+2][y:y+3])
            if max_power is None or energy > max_power:
                max_power = energy
                max_x = x
                max_y = y
    return (max_x, max_y)

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

    verify(highest_power_cordinate(18), (33,45))
    verify(highest_power_cordinate(42), (21,61))

if __name__ == "__main__":
    test_cases()
    print(execute())