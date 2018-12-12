#!/usr/bin/env python3

from collections import deque

def execute():
    # 400 players; last marble is worth 71864 points
    return marble_high_score(400, 71864), marble_high_score(400, 7186400)

def marble_high_score(players, last_marble, verbose = False):
    marble_circle = deque([0])
    current_index = 0
    scores = [0] * players
    for marble in range(1,last_marble+1):
        if marble % 23 == 0:
            winner = marble % players
            scores[winner] += marble
            marble_circle.rotate(7)
            scores[winner] += marble_circle.pop()
            marble_circle.rotate(-1)
        else:
            marble_circle.rotate(-1)
            marble_circle.append(marble)
        if verbose:
            print (marble_circle, marble_circle[current_index], scores)
        if marble % 10000 == 0:
            print(marble, " out of ", last_marble)
    return max(scores)

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

scores = """10 players; last marble is worth 1618 points: high score is 8317
13 players; last marble is worth 7999 points: high score is 146373
17 players; last marble is worth 1104 points: high score is 2764
21 players; last marble is worth 6111 points: high score is 54718
30 players; last marble is worth 5807 points: high score is 37305"""

def test_cases():
    verify(marble_high_score(9,25,True), 32)
    verify(marble_high_score(10,1618), 8317)
    verify(marble_high_score(13,7999), 146373)
    verify(marble_high_score(17,1104), 2764)
    verify(marble_high_score(21,6111), 54718)
    verify(marble_high_score(30,5807), 37305)

if __name__ == "__main__":
    test_cases()
    print(execute())