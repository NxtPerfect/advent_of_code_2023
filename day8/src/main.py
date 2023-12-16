import time
import math
from collections import defaultdict

# solution partly inspired by phase_rush


def find_match(start: str, directions: list, nodes: defaultdict):
    total = 0
    while start[2] != 'Z':
        for x in directions:
            if start[2] == 'Z':
                return total
            if x == 'L':
                start = nodes[start][0]
                total += 1
                continue
            start = nodes[start][1]
            total += 1
    return total


def part2(file="input.txt"):
    nodes: defaultdict = defaultdict(tuple)
    directions: list = list()
    starts: list = list()
    with open(file) as f:
        for i, line in enumerate(f):
            if i == 0:
                directions = [char for char in line.strip()]
                continue
            if i == 1:
                continue
            base, node = line.strip().split("=")
            left, right = node.strip().replace("(", '').replace(")", '').strip().split(", ")
            nodes[base.strip()] = (left.strip(), right.strip())
            if base.strip().endswith('A'):
                starts.append(base.strip())

    end = [find_match(x, directions, nodes) for x in starts]
    print(math.lcm(*end))
    return math.lcm(*end)


def run(file="input.txt"):
    total = 0
    nodes: defaultdict = defaultdict(tuple)
    directions: list = list()
    with open(file) as f:
        for i, line in enumerate(f):
            if i == 0:
                directions = [char for char in line.strip()]
                continue
            if i == 1:
                continue
            base, node = line.strip().split("=")
            left, right = node.strip().replace("(", '').replace(")", '').split(",")
            nodes[base.strip()] = (left.strip(), right.strip())
            # print(type(left), type(right))
            # print(left, right)
            # print(nodes.items())
    node = 'AAA'
    while node != 'ZZZ':
        # print(directions)
        for x in directions:
            # print(node, nodes[node], x, total)
            if node == 'ZZZ':
                break
            if x == 'L':
                node = nodes[node][0]
                total += 1
                continue
            node = nodes[node][1]
            total += 1
    print(total)
    return total


if __name__ == "__main__":
    start = time.perf_counter_ns()
    # minimum = run()
    minimum = part2()
    # print(minimum == 2)  # test
    # print(minimum == 6)  # edge
    # print(minimum == 6)  # test part 2
    # print(minimum == 6839)  # edge part 2
    end = time.perf_counter_ns()
    print(f'Runtime: {(end-start)/1_000_000} ms')
