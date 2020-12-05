#!/usr/bin/env python3

def execute():
    with open('2020/input/5.txt') as inp:
        lines = inp.readlines()
    seats = [l.strip() for l in lines if len(l.strip()) > 0]
    return get_max_id(seats), get_missing_id(seats)

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

def convert_from_binary(value, low="0", high="1"):
    return int(value.replace(low, "0").replace(high, "1"), 2)

def get_seat(seatref):
    return (convert_from_binary(seatref[:7], "F", "B"), convert_from_binary(seatref[-3:], "L", "R"))

def get_id(seatref):
    seat = get_seat(seatref)
    return seat[0]*8 + seat[1]

def get_max_id(seats):
    return max([get_id(seat) for seat in seats])

def get_missing_id(seats):
    sorted_seats = sorted([get_id(seat) for seat in seats])
    first_seat = sorted_seats[0]
    for i in range (1,len(sorted_seats)-1):
        if sorted_seats[i] != first_seat + i:
            return sorted_seats[i] - 1
    return -1

def test_cases():
    verify(get_seat("FBFBBFFRLR"), (44,5))
    verify(get_seat("BFFFBBFRRR"), (70,7))
    verify(get_seat("FFFBBBFRRR"), (14,7))
    verify(get_seat("BBFFBBFRLL"), (102,4))
    verify(get_id("FBFBBFFRLR"), 357)
    verify(get_id("BFFFBBFRRR"), 567)
    verify(get_id("FFFBBBFRRR"), 119)
    verify(get_id("BBFFBBFRLL"), 820)
    verify(get_max_id(["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]), 820)
    print("Failed {} out of {} tests. ".format(tests_failed, tests_executed))

if __name__ == "__main__":
    test_cases()
    print(execute())