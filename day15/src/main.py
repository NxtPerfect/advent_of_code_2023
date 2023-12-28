import time


def part1(file="input.txt"):
    strings: list = list()
    with open(file) as f:
        for line in f:
            strings = line.strip().split(',')
    print(strings)
    hash_val = 0
    for string in strings:
        hash_val_str = 0
        for char in string:
            hash_val_str = (hash_val_str + ord(char)) * 17 % 256
            # print(hash_val_str)
        hash_val += hash_val_str
        # print(hash_val)
    print(hash_val)
    return hash_val


def part2(file="test.txt"):
    with open(file) as f:
        for line in f:
            pass


if __name__ == "__main__":
    start = time.perf_counter_ns()
    p1 = part1()
    p2 = part2()
    # minimum = part2()
    # print(p1 == 1320)  # test
    # print(minimum == 1692591070)  # edge
    # print(maximum == 2)  # test part 2
    # print(minimum == 6839)  # edge part 2
    end = time.perf_counter_ns()
    print(f'Runtime: {(end-start)/1_000_000} ms')
