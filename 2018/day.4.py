#!/usr/bin/env python3

def execute():
    with open('input.4.txt') as inp:
        lines = inp.readlines()
    return guard_minute(l.strip() for l in lines if len(l.strip()) > 0)

def guard_minute(shifts):
    sorted_shifts = sorted(shifts)
    #print (sorted_shifts)
    guard = None
    total_sleep = {}
    sleep_pattern = {}
    sleep = 0
    wake = 0
    for shift in sorted_shifts:
        if shift[-5:] == "shift":
            guard = int(shift.split()[3][1:])
            #print("Guard", guard)
            if guard not in total_sleep:
                total_sleep[guard] = 0
                sleep_pattern[guard] = [0] * 60
        elif shift[-6:] == "asleep":
            sleep = int(shift[15:17])
            #print("asleep", sleep)
        elif shift[-2:] == "up":
            wake = int(shift[15:17])
            #print("awake", wake)
            total_sleep[guard] += wake - sleep
            #print (sleep, wake)
            for i in range(sleep, wake):
                sleep_pattern[guard][i] += 1
        # print(sleep_pattern)
    #print(total_sleep)
    #print(sleep_pattern)
    most_slept = (sorted(total_sleep, key=total_sleep.get)[-1])
    # print (most_slept, total_sleep[most_slept])
    index_max = max(range(0,len(sleep_pattern[most_slept])), key=sleep_pattern[most_slept].__getitem__)
    return most_slept * index_max

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (locals())

def test_cases():
    shifts = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""
    verify(guard_minute(shifts.split('\n')), 240)

if __name__ == "__main__":
    test_cases()
    print(execute())