#!/usr/bin/env python3

def execute():
    with open('2023/input/day.2.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return all_possible_games(data), total_power_of(data)

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

sample_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

max_color = {'red': 12, 'green': 13, 'blue': 14}

def possible_game(game):
    "Can these rounds be played with 12 red cubes, 13 green cubes, and 14 blue cubes?"
    game_id, rounds = game.split(': ')
    game_id = int(game_id.replace('Game ', ''))
    rounds = rounds.split('; ')
    for r in rounds:
        cubes = r.split(', ')
        for c in cubes:
            count, colour = c.split()
            if int(count) > max_color[colour]:
                return (game_id, False)
    return (game_id, True)

def minimum_cubes(game):
    min_cubes = {'red': 0, 'green': 0, 'blue': 0}
    game_id, rounds = game.split(': ')
    game_id = int(game_id.replace('Game ', ''))
    rounds = rounds.split('; ')
    for r in rounds:
        cubes = r.split(', ')
        for c in cubes:
            count, colour = c.split()
            min_cubes[colour] = max(min_cubes[colour], int(count))
    return min_cubes

def power_of(game):
    cubes = minimum_cubes(game)
    return cubes['red'] * cubes['green'] * cubes['blue']

def all_possible_games(games):
    validgames = [possible_game(g) for g in games]
    return sum([id for (id, valid) in validgames if valid])

def total_power_of(games):
    return sum([power_of(g) for g in games])

def test_cases():
    sample = sample_input.splitlines()
    verify(possible_game(sample[0]), (1, True))
    verify(possible_game(sample[1]), (2, True))
    verify(possible_game(sample[2]), (3, False))
    verify(possible_game(sample[3]), (4, False))
    verify(possible_game(sample[4]), (5, True))
    verify(all_possible_games(sample), 8)
    verify(power_of(sample[0]), 48)
    verify(power_of(sample[1]), 12)
    verify(power_of(sample[2]), 1560)
    verify(power_of(sample[3]), 630)
    verify(power_of(sample[4]), 36)
    verify(total_power_of(sample), 2286)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())