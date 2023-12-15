import time
from collections import defaultdict


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
    minimum = run()
    # print(minimum == 2)  # test
    print(minimum == 6)  # edge
    # print(minimum == 5905)  # test part 2
    # print(minimum == 6839)  # edge part 2
    end = time.perf_counter_ns()
    print("Runtime of " + str((end-start)/1000000) + "ms")
