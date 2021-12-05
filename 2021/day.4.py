#!/usr/bin/env python3

def execute():
    with open('./input/day.4.txt') as inp:
        lines = inp.readlines()
    data = [l.strip() for l in lines if len(l.strip()) > 0]
    return calculate_bingo_score(data)

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

example1 = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7""".splitlines()

def calculate_score(board):
    return sum([int(n) for n in board if n is not None])

def winning_row(board, pos):
    if pos < 5:
        return board[0:5] == [None] * 5
    if pos < 10:
        return board[5:10] == [None] * 5
    if pos < 15:
        return board[10:15] == [None] * 5
    if pos < 20:
        return board[15:20] == [None] * 5
    if pos < 25:
        return board[20:25] == [None] * 5

def winning_column(board, pos):
    return board[pos%5:25:5] == [None] * 5

def mark_boards(n, boards):
    for b in boards:
        if n in b:
            pos = b.index(n)
            b[pos] = None
            if winning_row(b, pos) or winning_column(b, pos):
                return calculate_score(b)
    return None

def play_bingo(numbers, boards):
    score = 0
    last_drawn = None
    for n in numbers:
        score = mark_boards(n, boards)
        if score is not None:
            last_drawn = int(n)
            break
    return (score, last_drawn)

def calculate_bingo_score(numbers_and_boards):
    numbers = numbers_and_boards[0].split(',')
    boards = []
    next_board = []
    for b in numbers_and_boards[1:]:
        if len(b) > 0:
            next_board += b.split()
            if len(next_board) == 25:
                boards.append(next_board)
                next_board = []
    (score, last_drawn) = play_bingo(numbers, boards)
    return score * last_drawn

def test_cases():
    verify(calculate_bingo_score(example1), 4512)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())