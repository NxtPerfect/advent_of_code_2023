from collections import defaultdict
import functools
import time

# SKIPPED
# I can't understand the solutions, i know what they're aiming for
# but i couldn't come up with it myself, i'll try again later

# Recursivelly call function onto the string, changing the first ? into . in first call and # in another call
# If we already failed the arrangement, abort from that call


@functools.lru_cache(maxsize=10000)
def part1(file: str = "test.txt"):
    total: int = 0
    check: defaultdict = defaultdict()
    with open(file) as f:
        for line in f:
            group, validation = line.strip().split(' ')
            check[group] = [int(x) for x in validation.strip().split(',')]
    print(check.items())

    for parts, checks in check.items():
        total += try_recursive_replace(parts, checks, 0)
    print(total)


def try_recursive_replace(parts: str, checks: list, curIndex: int):
    total = 0
    for idc, char in enumerate(parts[curIndex:]):
        group: int = 0
        if curIndex == len(parts):
            temp = parts.strip().split('.')
            for idx, x in enumerate(temp):
                if len(x) != checks[idx]:
                    return 0
            return 1
        if char in ['.', '#']:
            continue
            # If we already went over the amount
            # Edge case: what if we're on '#.#' and check is [1,1]
            # but we assume it's bad since the count is 2
            # Instead, let's just check if we're at the last char, then check
            # if string split by . has same count of '#' as check
        t = list(parts)[idc] = '.'
        t.join('')
        total += try_recursive_replace(t, checks, idc)
        t = list(parts)[idc] = '#'
        t.join('')
        total += try_recursive_replace(t, checks, idc)
    return total


def part2(file: str = "test.txt"):
    with open(file) as f:
        for line in f:
            pass


if __name__ == "__main__":
    start = time.perf_counter_ns()
    p1 = part1()
    p2 = part2()
    print(p1 == 21)  # test
    # print(minimum == 1692591070)  # edge
    # print(maximum == 2)  # test part 2
    # print(minimum == 6839)  # edge part 2
    end = time.perf_counter_ns()
    print(f'Runtime: {(end-start)/1_000_000} ms')
