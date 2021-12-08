#!/usr/bin/env python3

def execute():
    with open('./input/day.8.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return count_unique_number_segments(data), sum_all_outputs(data)

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

example0 = """acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf""".splitlines()

example1 = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce""".splitlines()

def count_unique(segment):
    return len([o for o in segment if len(o) in [2,3,4,7]])

def count_unique_number_segments(lines):
    segments = split_segments(lines)
    return sum([count_unique(o) for _, o in segments])

def split_segments(lines):
    segments = []
    for line in lines:
        i, o = line.split(' | ')
        segments.append( (i.split(' '), o.split(' ')) )
    return segments

bin_value = {'a': 1, 'b': 2, 'c': 4, 'd': 8, 'e': 16, 'f': 32, 'g': 64}

def get_hash(wires): #abcdefg
    return sum([bin_value[w] for w in wires])

def calculate_hash_segments(segments):
    h = {}
    lookup = {}
    for s in segments:
        if len(s) == 2:
            h[get_hash(s)] = 1
            lookup[1] = get_hash(s)
        elif len(s) == 3:
            h[get_hash(s)] = 7
            lookup[7] = get_hash(s)
        elif len(s) == 4:
            h[get_hash(s)] = 4
            lookup[4] = get_hash(s)
        elif len(s) == 7:
            h[get_hash(s)] = 8
            lookup[8] = get_hash(s)

    for s in segments:
        if get_hash(s) in h:
            continue
        elif len(s) == 5 and (get_hash(s) & lookup[7]) == lookup[7]:
            h[get_hash(s)] = 3
            lookup[3] = get_hash(s)
        elif len(s) == 6 and (get_hash(s) & lookup[4]) == lookup[4]:
            h[get_hash(s)] = 9
            lookup[9] = get_hash(s)
        elif len(s) == 6 and (get_hash(s) & lookup[7]) == lookup[7]:
            h[get_hash(s)] = 0
            lookup[0] = get_hash(s)
        elif len(s) == 6:
            h[get_hash(s)] = 6
            lookup[6] = get_hash(s)

    for s in segments:
        if get_hash(s) in h:
            continue
        if len(s) == 5 and (get_hash(s) & lookup[6]) == get_hash(s):
            h[get_hash(s)] = 5
            lookup[5] = get_hash(s)
        else:
            h[get_hash(s)] = 2
            lookup[2] = get_hash(s)
    return h

def get_output(segment):
    i, o = segment
    h = calculate_hash_segments(i)
    return (1000 * h[get_hash(o[0])]) + (100 * h[get_hash(o[1])]) + (10 * h[get_hash(o[2])]) + h[get_hash(o[3])]

def sum_all_outputs(lines):
    return sum([get_output(s) for s in split_segments(lines)])

def test_cases():
    verify(count_unique_number_segments(example1), 26)
    verify(get_output(split_segments(example0)[0]), 5353)
    verify(sum_all_outputs(example1), 61229)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())