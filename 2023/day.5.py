#!/usr/bin/env python3

def execute():
    with open('2023/input/day.5.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines]
    return lowest_location(parse(data))

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

sample_input = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".splitlines()

def parse(almanac):
    alm = {}
    this_map = None
    for l in almanac:
        if l.startswith('seeds:'):
            alm['seeds'] = [int(i) for i in l[6:].split()]
        elif l.endswith('map:'):
            this_map = l[:-5]
            alm[this_map] = []
        elif len(l.strip()) == 0:
            this_map = None
        else:
            line = [int(i) for i in l.split()]
            alm[this_map].append(line)
    return alm

def get_seeds(alm):
    return alm['seeds']

def get_soil(alm):
    seeds = get_seeds(alm)
    return translate(seeds, alm['seed-to-soil'])

def get_locations(alm):
    nxt = get_soil(alm)
    for mapping in ['soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']:
        nxt = translate(nxt, alm[mapping])
    return nxt

def lowest_location(almanac):
    return min(get_locations(almanac))

def translate(src, mapping):
    if type(src) == type([]):
        return [translate(s, mapping) for s in src]
    for m in mapping:
        dest_start, src_start, range_len = m
        if src >= src_start and src < src_start + range_len:
            return dest_start + (src - src_start)
    return src

def test_cases():
    alm = parse(sample_input)
    verify(translate([0], alm['seed-to-soil']), [0])
    verify(translate([1], alm['seed-to-soil']), [1])
    verify(translate([48], alm['seed-to-soil']), [48])
    verify(translate([49], alm['seed-to-soil']), [49])
    verify(translate([50], alm['seed-to-soil']), [52])
    verify(translate([51], alm['seed-to-soil']), [53])
    verify(translate([96], alm['seed-to-soil']), [98])
    verify(translate([97], alm['seed-to-soil']), [99])
    verify(translate([98], alm['seed-to-soil']), [50])
    verify(translate([99], alm['seed-to-soil']), [51])
    verify(get_seeds(alm), [79, 14, 55, 13])
    verify(get_soil(alm), [81, 14, 57, 13])
    verify(get_locations(alm), [82, 43, 86, 35])
    verify(lowest_location(alm), 35)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())