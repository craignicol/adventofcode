#!/usr/bin/env python3

def execute():
    with open('input.13.txt') as inp:
        lines = inp.readlines()
    return first_crash_location(lines)

turn_cycle = ['l', 's', 'r']
next_turn = {'l':'s', 's':'r', 'r':'l'}

def get_train_locations(track):
    trains = []
    y = 0
    for row in track:
        x = 0
        for ch in row:
            if ch in ['v', '<', '>', '^']:
                trains.append((x,y,ch,'l'))
            x += 1
        y += 1
    return trains

def remove_trains(track):
    return [r.replace('>','-').replace('<', '-').replace('v', '|').replace('^', '|').replace('\n', '') for r in track]

def train_at(x, y, trains):
    return len([(tx, ty) for (tx, ty, _, _) in trains if x == tx and y == ty]) > 0

vectors = {'v' : (0, 1), '<': (-1, 0), '>': (1, 0), '^': (0, -1)}
directions = {
    'v':{'l':'>', 's':'v', 'r':'<', '/':'<', '\\':'>'}, 
    '<':{'l':'v', 's':'<', 'r':'^', '/':'v', '\\':'^'}, 
    '>':{'l':'^', 's':'>', 'r':'v', '/':'^', '\\':'v'}, 
    '^':{'l':'<', 's':'^', 'r':'>', '/':'>', '\\':'<'}}


def next_move(track, trains):
    crashed = None
    trains = sorted_trains(trains) # left to right, top to bottom
    new_trains = []
    for (x, y, direction, intersection_direction) in trains[:]:
        vector = vectors[direction]
        (target_x, target_y) = (x + vector[0], y + vector[1])
        if (train_at(target_x, target_y, trains) and direction in ['>', 'v']) or train_at(target_x, target_y, new_trains):
            crashed = (target_x, target_y)
            break
        elif track[target_y][target_x] in [' ']:
            print("WTF", x, y, direction, intersection_direction)
            crashed = (target_x, target_y)
            break
        elif track[target_y][target_x] in ['|', '-']:
            new_trains.append((target_x, target_y, direction, intersection_direction))
        elif track[target_y][target_x] == '+':
            new_direction = directions[direction][intersection_direction]
            new_int_direction = next_turn[intersection_direction]
            new_trains.append((target_x, target_y, new_direction, new_int_direction))
        elif track[target_y][target_x] in ['/', '\\']:
            new_direction = directions[direction][track[target_y][target_x]]
            new_trains.append((target_x, target_y, new_direction, intersection_direction))
        else:
            print("I'm lost!")
            crashed = (target_x, target_y)
            break
        
    return (new_trains, crashed)

def first_crash_location(track):
    trains = get_train_locations(track)
    track = remove_trains(track)
    print('\n'.join(track))
    crashed = None
    while crashed is None: 
        (trains, crashed) = next_move(track, trains)
    return crashed

def sorted_trains(trains):
    return sorted(trains, key=lambda x: x[0] + 1000 * x[1])

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    trains = [(143, 15, '^', 'l'), (120, 29, 'v', 'l'), (84, 45, 'v', 'l'), (78, 49, '^', 'l'), (94, 58, '<', 'l'), (2, 65, 'v', 'l'), (97, 65, '<', 'l'), (121, 86, '^', 'l'), (112, 93, 'v', 'l'), (80, 101, '>', 'l'), (120, 105, '^', 'l'), (60, 108, 'v', 'l'), (126, 118, '>', 'l'), (42, 131, 'v', 'l'), (38, 142, '>', 'l'), (85, 142, '>', 'l'), (100, 147, '>', 'l')]
    verify(sorted_trains(trains), trains)
    verify(train_at(0, 0, [(0,0,None,None)]), True)
    verify(train_at(0, 0, [(0,1,None,None)]), False)

    input_track = r"""
/->-\        
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   """
    verify(first_crash_location(input_track.split('\n')[1:]), (7, 3))

if __name__ == "__main__":
    test_cases()
    print(execute())