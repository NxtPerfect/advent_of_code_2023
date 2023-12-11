from collections import defaultdict
import time
import math

# That will ensure our win, even if it's by a fraction
# Time is in milliseconds, distance in millimiters
# For each unit of time we spend holding button, our speed increases by 1 time/distance
# Find all the combinations that still beat the record


def run(file="input.txt"):
    race = defaultdict(int)
    ways = list()

    with open(file) as f:
        data = f.readlines()

    tempTimes = data[0].strip().split(" ")
    # tempTimes = list(filter(lambda x: x != '' or x != 'Time:', tempTimes))
    tTimes = [x for x in tempTimes if x != '' and x != 'Time:']
    tempTimes = map(int, tTimes)
    tempDistance = data[1].strip().split(" ")
    tDist = [x for x in tempDistance if x != '' and x != 'Distance:']
    tempDistance = map(int, tDist)

    race = {key: value for key, value in zip(tempTimes, tempDistance)}

    for key, value in race.items():
        curWays = list()
        for x in range(1, key-1):
            if x * (key - x) <= value:
                continue
            curWays.append(x)
        ways.append(len(curWays))

    print(tempTimes, tempDistance)
    print(race)
    print(ways)
    print(math.prod(ways))
    return math.prod(ways)


if __name__ == "__main__":
    start = time.perf_counter_ns()
    minimum = run()
    print("Is it correct?", minimum == 288)
    # print("Is it correct?", minimum == 71503)
    end = time.perf_counter_ns()
    print("Runtime of " + str((end-start)/1000000) + "ms")
