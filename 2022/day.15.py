#!/usr/bin/env python3

def execute():
    with open('2022/input/day.15.txt') as inp:
        lines = inp.readlines()
    data = parse_sensor_map([l.strip() for l in lines if len(l.strip()) > 0])
    return covered_in_row(data, 2000000)[0],tuning_frequency(data)

tests_failed = 0
tests_executed = 0

def verify(a, b):
    global tests_executed
    global tests_failed

    tests_executed += 1
    if (a == b):
        print("✓")
        return
    
    tests_failed += 1
    print (locals())

sample_input = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3""".splitlines()

def parse_sensor_map(sensor_map):
    sensors = []
    for sensor in sensor_map:
        s, b = sensor.split(':')
        x, y = s.split('Sensor at x=')[1].split(',')[0:2]
        x = int(x)
        y = int(y[3:])
        x2, y2 = b.split('closest beacon is at x=')[1].split(',')[0:2]
        x2 = int(x2)
        y2 = int(y2[3:])
        sensors.append(((x, y), (x2, y2)))
    return sensors

def covered_in_row(sensor_map, row):
    covered = []
    for s, b in sensor_map:
        # determine scan area
        diamonddist = abs(s[0] - b[0]) + abs(s[1] - b[1])
        if s[1] - diamonddist <= row <= s[1] + diamonddist:
            # determine scan area
            x1 = (s[0] - diamonddist) + abs(s[1] - row)
            x2 = (s[0] + diamonddist) - abs(s[1] - row)
            covered.append((x1, x2))
    comparator = lambda a: a[0]
    covered.sort(key=comparator)
    # merge overlapping areas
    i = 0
    while i < len(covered) - 1:
        if covered[i][1] >= covered[i+1][0]:
            covered[i] = (covered[i][0], max(covered[i][1], covered[i+1][1]))
            covered.pop(i+1)
        else:
            i += 1
    return sum([b - a for (a,b) in covered]), covered

def tuning_frequency(sensor_map):
    location = (0, 0)
    area = (0, 0, 0, 0)
    for s, b in sensor_map:
        if s[0] > area[2]:
            area = (area[0], area[1], s[0], area[3])
        if s[0] < area[0]:
            area = (s[0], area[1], area[2], area[3])
        if s[1] > area[3]:
            area = (area[0], area[1], area[2], s[1])
        if s[1] < area[1]:
            area = (area[0], s[1], area[2], area[3])

    for row in range(area[1], area[3] + 1):
        _, covered = covered_in_row(sensor_map, row)
        if len(covered) > 1:
            location = (covered[0][1] + 1, row)
            break
    # print(diamond_dist)
    return location[0] * 4000000 + location[1]

def test_cases():
    sensor_map = parse_sensor_map(sample_input)
    verify(sensor_map[0], ((2, 18), (-2, 15)))
    verify(covered_in_row(sensor_map, 10)[0], 26)
    verify(tuning_frequency(sensor_map), 56000011)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())