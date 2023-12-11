import time


def run(file="input.txt"):
    ways = 0

    with open(file) as f:
        data = f.readlines()

    tempTimes = int("".join(data[0].strip().split(":")[1].split()))
    tempDistance = int("".join(data[1].strip().split(":")[1].split()))

    # I don't know exact function, but this one is pretty close
    x = int(tempTimes/tempDistance * tempDistance/4.9)
    while True:
        if x * (tempTimes - x) <= tempDistance:
            x += 1
            continue
        diff = x
        ways = (tempTimes - 2*diff + 1)
        break

    # print(ways)
    return ways


if __name__ == "__main__":
    start = time.perf_counter_ns()
    minimum = run()
    end = time.perf_counter_ns()
    print("Runtime of " + str((end-start)/1000000) + "ms")
