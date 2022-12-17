#!/usr/bin/env python3

import re


def execute():
    with open('2022/input/day.16.txt') as inp:
        lines = inp.readlines()
    data = parse_valves([l.strip() for l in lines if len(l.strip()) > 0])
    return best_flow(data)

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

sample_input = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
Valve BB has flow rate=13; tunnels lead to valves CC, AA
Valve CC has flow rate=2; tunnels lead to valves DD, BB
Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
Valve EE has flow rate=3; tunnels lead to valves FF, DD
Valve FF has flow rate=0; tunnels lead to valves EE, GG
Valve GG has flow rate=0; tunnels lead to valves FF, HH
Valve HH has flow rate=22; tunnel leads to valve GG
Valve II has flow rate=0; tunnels lead to valves AA, JJ
Valve JJ has flow rate=21; tunnel leads to valve II""".splitlines()

def parse_valves(lines):
    regex = re.compile(r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.*)')
    valves = {}
    for line in lines:
        m = regex.match(line)
        name, flow, tunnels = m.groups()
        flow = int(flow)
        tunnels = tunnels.split(', ')
        valves[name] = {'flow_rate': flow, 'tunnels': tunnels}
    return valves

class route:
    def __init__(self) -> None:
        self.open = set()
        self.current = 'AA'
        self.flow = 0
        self.history = []
        self.flowhistory = []
        self.visited = set(['AA'])

def best_flow(valves):
    best = []
    current = 'AA'
    routes = [route()]
    for i in range(30):
        new_routes = []
        for r in routes:
            flow_now = sum([valves[v]['flow_rate'] for v in r.open]) 
            r.flow += flow_now
            r.flowhistory.append(flow_now)
            if r.current in valves:
                for tunnel in valves[r.current]['tunnels']:
                    new_route = route()
                    new_route.open = r.open.copy()
                    new_route.current = tunnel
                    new_route.flow = r.flow
                    new_route.flowhistory = r.flowhistory.copy()
                    new_route.history = r.history.copy()
                    new_route.history.append('tunnelled to ' + tunnel)
                    new_route.visited = r.visited.copy()
                    new_route.visited.add(tunnel)
                    new_routes.append(new_route)
            if r.current not in r.open and valves[r.current]['flow_rate'] > 0:
                    r.open.add(r.current)
                    r.history.append(r.current + ' opened')
                    new_routes.append(r)
        routes = sorted(new_routes, key=lambda r: r.flow + (2*len(r.open)) + len(r.visited), reverse=True)[:1000]
    return max([r.flow for r in routes])

def test_cases():
    valves = parse_valves(sample_input)
    verify(valves['AA']['flow_rate'], 0)
    verify(valves['AA']['tunnels'], ['DD', 'II', 'BB'])
    verify(best_flow(valves), 1651)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())