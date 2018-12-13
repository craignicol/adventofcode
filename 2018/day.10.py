#!/usr/bin/env python3

from collections import Counter

def execute():
    with open('input.10.txt') as inp:
        lines = inp.readlines()
    for frame in animate_keyframes([l.strip() for l in lines if len(l.strip()) > 0]):
        print(frame)

# frame is always square
def extend_frame(frame, extent):
    limit = (extent * 2) + 1
    new_frame = ['.' * limit for i in range(limit)]
    if frame is not None:
        offset = extent - (len(frame) // 2)
        row_num = 0
        for row in frame:
            new_frame[offset + row_num] = ('.' * offset) + row + ('.' * offset)
            row_num += 1
    return new_frame

def render_frame(pos_vel, abs_max_value = 2, frame_num = 1):
    frame = extend_frame(None, abs_max_value)
    for (pos, vel) in pos_vel:
        (right, down) = pos
        extent = max(abs(right), abs(down))
        if extent * 2 > len(frame):
            frame = extend_frame(frame, extent)
        origin = (len(frame) // 2)
        frame[origin+down] = frame[origin+down][:origin+right] + '#' + frame[origin+down][origin+right+1:]
    with open("output.10.f" + str(frame_num) + ".txt", "w") as f:
        f.write('\n'.join(frame))
    return "."

def animate(pos_vel):
    result = []
    for (pos, vel) in pos_vel:
        result.append(((pos[0]+vel[0], pos[1]+vel[1]), vel))
    return result
    
# Keyframe if column contains 7 stars 
def is_key_frame(pos_vel):
    result = True
    count = Counter([p[0] for (p,v) in pos_vel])
    if max(count.values()) > 6:
        return True
    return False

def animate_keyframes(position_velocity):
    pos_vel = []
    abs_max_value = 0
    for pv in position_velocity:
        pv = pv.replace('>', '<')
        (pos_txt, pos, vel_txt, vel, end_txt) = pv.split('<')
        pos = [int(i) for i in pos.split(',')] 
        vel = [int(i) for i in vel.split(',')]
        pos_vel.append(((pos[0], pos[1]), (vel[0], vel[1])))
        extent = max(abs(pos[0]), abs(pos[1]))
        if extent > abs_max_value:
            abs_max_value = extent
    frames = []
    for i in range(5):
        if is_key_frame(pos_vel):
            frames.append(render_frame(pos_vel, abs_max_value, i))
        pos_vel = animate(pos_vel)
    return frames

def verify(a, b):
    if (a == b):
        print("✓")
        return
    
    print (a, '\n'.join(['', '---', '']), b)

def test_cases():
    test_input = """position=< 9,  1> velocity=< 0,  2>
position=< 7,  0> velocity=<-1,  0>
position=< 3, -2> velocity=<-1,  1>
position=< 6, 10> velocity=<-2, -1>
position=< 2, -4> velocity=< 2,  2>
position=<-6, 10> velocity=< 2, -2>
position=< 1,  8> velocity=< 1, -1>
position=< 1,  7> velocity=< 1,  0>
position=<-3, 11> velocity=< 1, -2>
position=< 7,  6> velocity=<-1, -1>
position=<-2,  3> velocity=< 1,  0>
position=<-4,  3> velocity=< 2,  0>
position=<10, -3> velocity=<-1,  1>
position=< 5, 11> velocity=< 1, -2>
position=< 4,  7> velocity=< 0, -1>
position=< 8, -2> velocity=< 0,  1>
position=<15,  0> velocity=<-2,  0>
position=< 1,  6> velocity=< 1,  0>
position=< 8,  9> velocity=< 0, -1>
position=< 3,  3> velocity=<-1,  1>
position=< 0,  5> velocity=< 0, -1>
position=<-2,  2> velocity=< 2,  0>
position=< 5, -2> velocity=< 1,  2>
position=< 1,  4> velocity=< 2,  1>
position=<-2,  7> velocity=< 2, -2>
position=< 3,  6> velocity=<-1, -1>
position=< 5,  0> velocity=< 1,  0>
position=<-6,  0> velocity=< 2,  0>
position=< 5,  9> velocity=< 1, -2>
position=<14,  7> velocity=<-2,  0>
position=<-3,  6> velocity=< 2, -1>"""
    test_output = """......................
......................
......................
......................
......#...#..###......
......#...#...#.......
......#...#...#.......
......#####...#.......
......#...#...#.......
......#...#...#.......
......#...#...#.......
......#...#..###......
......................
......................
......................
......................"""
    verify(animate_keyframes(test_input.split('\n'))[0], test_output)

if __name__ == "__main__":
    test_cases()
    execute()