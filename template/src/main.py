import time


def run(file="input.txt"):
    with open(file) as f:
        for line in f:
            pass


if __name__ == "__main__":
    start = time.perf_counter_ns()
    minimum = run()
    # maximum = part2()
    # minimum = part2()
    print(minimum == 4)  # test
    # print(minimum == 1692591070)  # edge
    # print(maximum == 2)  # test part 2
    # print(minimum == 6839)  # edge part 2
    end = time.perf_counter_ns()
    print(f'Runtime: {(end-start)/1_000_000} ms')
