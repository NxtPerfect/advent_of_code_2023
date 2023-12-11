import time


def run(file="input.txt"):
    ways = 0

    with open(file) as f:
        data = f.readlines()

    tempTimes = int("".join(data[0].strip().split(":")[1].split()))
    tempDistance = int("".join(data[1].strip().split(":")[1].split()))

    # 0,1,2,...x,...key-x
    x = int(tempTimes/tempDistance * tempDistance/4.9)
    while True:
        # for x in range(1, key-1):
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
    # print("Is it correct?", minimum == 288)
    # print("Is it correct?", minimum == 71503)
    end = time.perf_counter_ns()
    print("Runtime of " + str((end-start)/1000000) + "ms")
