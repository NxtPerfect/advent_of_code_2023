import time
from collections import defaultdict


def part1(file="input.txt"):
    strings: list = list()
    with open(file) as f:
        for line in f:
            strings = line.strip().split(',')
    hash_val = 0
    for string in strings:
        hash_val_str = 0
        for char in string:
            hash_val_str = (hash_val_str + ord(char)) * 17 % 256
            # print(hash_val_str)
        hash_val += hash_val_str
        # print(hash_val)
    # print(hash_val)
    return hash_val


def part2(file="input.txt"):
    boxes: defaultdict = defaultdict(list)
    strings: list = list()
    with open(file) as f:
        for line in f:
            strings = line.strip().split(',')
    total = 0
    for string in strings:
        hash_val_str = 0
        for char in string:
            if char == '-':
                if any(string.split('-')[0] in x for x in boxes[hash_val_str]):
                    # print(hash_val_str)
                    # print(string[:2], 'found')
                    for item in boxes[hash_val_str]:
                        # print(item)
                        if string.split('-')[0] in item:
                            boxes[hash_val_str].remove(item)
                            break
                    break
                # print(boxes[hash_val_str])
                # print(string[:2], 'not in boxes')
                break
            if char == '=':
                if any(string.split('=')[0] in x for x in boxes[hash_val_str]):
                    for x in boxes[hash_val_str]:
                        if string.split('=')[0] == x[0]:
                            x[1] = string.split('=')[1]
                            break
                    break
                boxes[hash_val_str].append(
                    [string.split('=')[0], string.split('=')[1]])
                # print(hash_val_str)
                break
            hash_val_str = (hash_val_str + ord(char)) * 17 % 256
            # print(hash_val_str)
        # print(boxes.items())
    for x in boxes.items():
        for idy, y in enumerate(x[1]):
            total += (int(x[0]) + 1) * (idy + 1) * int(y[1])
    print(total)
    return total


if __name__ == "__main__":
    start = time.perf_counter_ns()
    p1 = part1()
    p2 = part2()
    # print(p1 == 1320)  # test
    print(p2 == 145)  # test part 2
    # print(p2 == 6839)  # edge part 2
    end = time.perf_counter_ns()
    print(f'Runtime: {(end-start)/1_000_000} ms')
