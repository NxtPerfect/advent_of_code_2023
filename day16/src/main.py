import time
from collections import defaultdict


def part1(file="test.txt"):
    cave: defaultdict = defaultdict()
    with open(file) as f:
        for i, line in enumerate(f):
            cave[i] = [x for x in line.strip()]

    print(cave.items())
    total: int = 0
    x, y = 0, 0
    # while x < len(cave[y]) or y < len(cave):
    total += walkHorizontal(x, y, cave, False)
    print(total)
    return total


# WIP
# Function that walks both up down and left right
def walk(x: int, y: int, cave: defaultdict, direction: int):
    total: int = 0
    visited: list = []
    while True:
        if (x == 0 and direction == -1) or (x == len(cave[y])-1 and direction == 1) or (y == 0 and direction == -2) or (y == len(cave)-1 and direction == 2):
            return total + 1
        if (x, y) in visited:
            return total
        cave[y][x] = '#'
        x += direction if direction % 2 != 0 else 0
        y += direction // 2 if direction % 2 == 0 else 0

        if direction % 2 != 0:
            pass


def walkHorizontal(x: int, y: int, cave: defaultdict, reverse: bool):
    total: int = 0
    direction: int = 1 if not reverse else -1
    while True:
        # Check if first run, check if x == 1
        if (x == 0 and direction == -1) or (x == len(cave[y]) - 1 and direction == 1):
            return total + 1
        # Out of bounds check
        if x + direction > len(cave[y]) - 1 or x + direction < 0:
            return total
        # Precalculate total and direction
        total += 1
        print('x:', x, 'y:', y, 'total:', total, 'HORIZONTAL')
        cave[y][x] = '#'
        x += direction
        if cave[y][x] in ['.', '-']:
            continue
        if cave[y][x] == '|':
            total += 1
            total += walkVertical(x, y, cave, True)  # walk upwards
            total += walkVertical(x, y, cave, False)  # walk downwards
            return total
        # If going from right to left
        if cave[y][x] == '\\':
            total += 1
            # walk upwards
            total += walkVertical(x, y, cave, direction == -1)
            return total
        if cave[y][x] == '/':
            total += 1
            # walk downwards
            total += walkVertical(x, y, cave, direction == 1)
            return total
        return total


def walkVertical(x: int, y: int, cave: defaultdict, reverse: bool):
    total: int = 0
    direction: int = 1 if not reverse else -1
    while True:
        # Check if first run, check if y == 1
        if (y == 0 and direction == -1) or (y == len(cave) - 1 and direction == 1):
            return total + 1
        # Out of bounds check
        if y + direction > len(cave) - 1 or y + direction < 0:
            return total
        # Precalculate total and direction
        total += 1
        print('x:', x, 'y:', y, 'total:', total, 'VERTICAL')
        cave[y][x] = '#'
        y += direction
        if cave[y][x] in ['.', '|']:
            continue
        if cave[y][x] == '-':
            total += 1
            total += walkHorizontal(x, y, cave, True)  # walk left
            total += walkHorizontal(x, y, cave, False)  # walk right
            return total
        # If going from bottom to top
        if cave[y][x] == '\\':
            # walk left
            total += 1
            total += walkHorizontal(x, y, cave, direction == -1)
            return total
        if cave[y][x] == '/':
            # walk right
            total += 1
            total += walkHorizontal(x, y, cave, direction == 1)
            return total
        return total


def part2(file="test.txt"):
    with open(file) as f:
        for line in f:
            pass


if __name__ == "__main__":
    start = time.perf_counter_ns()
    # p1 = part1()
    # p2 = part2()
    # print(part1('test.txt') == 46)  # test
    print(part1('edge.txt') == 11)  # edge
    # print(part1('input.txt')) # input
    # print(part2('test.txt') == 2)  # test part 2
    # print(part2('edge.txt') == 6839)  # edge part 2
    # print(part2('input.txt')) # input
    end = time.perf_counter_ns()
    print(f'Runtime: {(end-start)/1_000_000} ms')
