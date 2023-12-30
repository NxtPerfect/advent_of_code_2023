import time


def part1(file="test.txt"):
    with open(file) as f:
        for line in f:
            pass


def part2(file="test.txt"):
    with open(file) as f:
        for line in f:
            pass


if __name__ == "__main__":
    start = time.perf_counter_ns()
    p1 = part1()
    p2 = part2()
    print(part1('test.txt') == 4)  # test
    print(part1('edge.txt') == 1692591070)  # edge
    print(part2('test.txt') == 2)  # test part 2
    print(part2('edge.txt') == 6839)  # edge part 2
    end = time.perf_counter_ns()
    print(f'Runtime: {(end-start)/1_000_000} ms')
