#!/usr/bin/env python3

def execute():
    with open('2022/input/day.7.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return sum_of_less_than(create_tree(data), 100000)

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

sample_input = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".splitlines()

def create_tree(lines):
    d = {'/': 0}
    cwd = []
    for line in lines:
        if line.strip() == '':
            continue
        elif line.startswith('$ cd'):
            path = line[5:]
            if path == '/':
                cwd = []
            elif path == "..":
                cwd.pop()
            else:
                cwd.append(path)
        elif line.startswith('$ ls'):
            continue
        elif line.startswith('dir'):
            path = '/'.join(cwd) + '/' + line[4:]
            if path[0] != '/':
                path = '/' + path
            if path not in d:
                d[path] = 0
        else:
            size = int(line.split()[0])
            path = ''
            d['/'] += size
            for p in cwd:
                path = path + '/' + p 
                d[path] += size
    return d

def sum_of_less_than(d, size):
    return sum([v for k, v in d.items() if v < size])

def test_cases():
    d = create_tree(sample_input)
    verify(d['/'], 48381165)
    verify(d['/a'], 94853)
    verify(d['/a/e'], 584)
    verify(d['/d'], 24933642)
    verify(sum_of_less_than(d, 100000), 95437)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())