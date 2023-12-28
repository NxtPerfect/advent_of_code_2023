from collections import defaultdict
import time

# For horizontal
# - check if current line = previous line
# - if yes, that's the reflection, now ignore the line that is further away
# as if it's asymetrical, we take the minimum distance, and anything more is out of reflection
# then multiply number of rows above by 100
# For vertical
# - check if current char == char on the other side
# - if yes, check next char and char on the other side -1 pos
# - continue until the index of first char - index of second is 1
# add columns to the left

# Divide input if line = '\n'
# We need to pass that data into both functions, and if no matches found, return 0

# Maybe i can just look up on dict
# take each element, see if it's in the dict, if it is then that's the mirror
# do it when we're reading input


def part1(file="test.txt"):
    total: int = 0
    data: defaultdict = defaultdict(list)
    with open(file) as f:
        idx = 0
        for line in f:
            if line == '\n':
                idx += 1
                continue
            data[idx].append(line.strip())
    print(data.values())
    mirror_index = len(data[0])-1
    for mirrors in data.values():
        # Horizontal line
        for idx, line in enumerate(mirrors):
            if line != mirrors[mirror_index]:
                continue
            if abs(mirror_index - idx) == 1:
                break
            mirror_index -= 1  # If our current line from top is equal line from bottom
            # then we need to check line on the bottom that's one higher
        if mirror_index == len(mirrors)-1:
            mirror_index = 0
        total += mirror_index * 100
        print(total)
        total += vertical(mirrors)
    print(total)
    return total


def vertical(data=[]):
    # Vertical line
    mirror_index: int = len(data)-1
    for idx, char in enumerate(data):
        # print(mirror_index)
        if char != data[mirror_index]:
            # print('Char: ', char, idx, '!= ', data[
            #       mirror_index], mirror_index)
            continue
        # print('Char: ', char, idx, '== ', data[
        #       mirror_index], mirror_index)
        if abs(mirror_index - idx) == 1:
            break
        mirror_index -= 1
    if mirror_index == len(data)-1:
        mirror_index = 0
    # print(mirror_index)
    return mirror_index


def part2(file="test.txt"):
    with open(file) as f:
        for line in f:
            pass


if __name__ == "__main__":
    start = time.perf_counter_ns()
    p1 = part1()
    p2 = part2()
    # minimum = part2()
    print(p1 == 405)  # test
    # print(p1 == 1692591070)  # edge
    # print(p2 == 2)  # test part 2
    # print(p2 == 6839)  # edge part 2
    end = time.perf_counter_ns()
    print(f'Runtime: {(end-start)/1_000_000} ms')
