# ----
# SKIPPED
# I don't understand the solutions yet and i'm having a lot of trouble trying to figure it out
# will try and come back to it later

import time

# Start from 'S' and go towards the right side
# Simulatnously go towards the left side
# When we have those two points meet, that's the farthest point

char_map = {"|": [(0, 1), (0, -1)], "-": [(1, 0), (-1, 0)], 'L': [(0, 1), (1, 0)], 'J': [(0, 1), (-1, 0)],
            '7': [(0, -1), (-1, 0)], 'F': [(0, -1), (1, 0)], '.': [], 'S': [(0, 1), (0, -1), (1, 0), (-1, 0)]}


def find_valid_move():
    pass


def run(file="test.txt"):
    data = open(file).read().strip()
    for y, line in enumerate(data):
        startpos = line.find('S')
        if startpos < 0:
            continue
        x1, y1 = startpos, y
    grid = [[x for x in row] for row in data.strip().split("\n")]
    find_valid_move()


if __name__ == "__main__":
    start = time.perf_counter_ns()
    minimum = run()
    # maximum = part2()
    # minimum = part2()
    print(minimum == 4)  # test
    # print(minimum == 8)  # edge
    # print(maximum == 2)  # test part 2
    # print(minimum == 6839)  # edge part 2
    end = time.perf_counter_ns()
    print(f'Runtime: {(end-start)/1_000_000} ms')
