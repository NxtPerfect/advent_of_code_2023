from collections import defaultdict
import time


def run(file="input.txt"):
    # Part two
    count = defaultdict(initDict)
    with open(file) as f:
        for idx, line in enumerate(f):
            game, numb = line.strip().split(":")
            winner, sample = numb.strip().split("|")
            sample = sample.strip().split()
            winner = winner.strip().split()

            numb_intersections = len(set(winner).intersection(set(sample)))

            for update in range(numb_intersections):
                count[idx+1+update] += count[idx]

    print(sum(count.values()))


def initDict():
    return 1


if __name__ == "__main__":
    start = time.perf_counter_ns()
    run()
    end = time.perf_counter_ns()
    print("Runtime of " + str((end-start)/1000000) + "ms")
