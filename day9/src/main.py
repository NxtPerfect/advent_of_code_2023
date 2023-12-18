from collections import defaultdict
import time


def run(file="input.txt"):
    total: int = 0
    values: defaultdict = defaultdict(list)
    oasis: defaultdict = defaultdict(list)
    with open(file) as f:
        i = 0
        for idx, line in enumerate(f):
            values[idx] = [int(x) for x in line.strip().split(" ")]
            if values[idx] not in oasis[idx]:
                oasis[idx+i] = values[idx]
            i += 1
            for x, y in zip(values[idx], values[idx][1::]):
                oasis[idx+i].append(y-x)
                # print(x, y, oasis)
            while True:
                oasis[idx+i+1] = calculateNextLine(oasis[idx+i])
                if not any(oasis[idx+i+1]):
                    i += 1
                    break
                i += 1
            # print(oasis)
    temp: list = list()
    for x in oasis.values():
        # print(x, temp)
        if not any(x):
            # print("Before adding total is ", total)
            temp.append(0)
            temp.reverse()
            total += predict(temp)
            # print("After adding ", total)
            temp = list()
            continue
        temp.append(x[-1])
    print(total)
    return total


def part2(file="input.txt"):
    total: int = 0
    values: defaultdict = defaultdict(list)
    oasis: defaultdict = defaultdict(list)
    with open(file) as f:
        i = 0
        for idx, line in enumerate(f):
            values[idx] = [int(x) for x in line.strip().split(" ")]
            if values[idx] not in oasis[idx]:
                oasis[idx+i] = values[idx]
            i += 1
            for x, y in zip(values[idx], values[idx][1::]):
                oasis[idx+i].append(y-x)
                # print(x, y, oasis)
            while True:
                oasis[idx+i+1] = calculateNextLine(oasis[idx+i])
                if not any(oasis[idx+i+1]):
                    i += 1
                    break
                i += 1
            # print(oasis)
    temp: list = list()
    for x in oasis.values():
        # print(x, temp)
        if not any(x):
            # print("Before adding total is ", total)
            temp.append(0)
            temp.reverse()
            total += predictPart2(temp)
            # print("After adding ", total)
            temp = list()
            continue
        temp.append(x[0])
    print(total)
    return total


def calculateNextLine(values: list):
    temp: list = list()
    for x, y in zip(values, values[1::]):
        temp.append(y-x)
    return temp


def predict(values: list):
    temp: list = list()
    # values.append(0)
    # values.reverse()
    for i, item in enumerate(values):
        if i == 0:
            temp.append(0)
            continue
        temp.append(temp[i-1] + item)
    print(temp)
    return temp[-1]


def predictPart2(values: list):
    temp: list = list()
    # values.append(0)
    # values.reverse()
    for i, item in enumerate(values):
        if i == 0:
            temp.append(0)
            continue
        temp.append(item - temp[i-1])
    # print(temp)
    return temp[-1]


if __name__ == "__main__":
    start = time.perf_counter_ns()
    # minimum = run()
    maximum = part2()
    # minimum = part2()
    # print(minimum == 114)  # test
    # print(minimum == 1692591070)  # edge
    print(maximum == 2)  # test part 2
    # print(minimum == 6839)  # edge part 2
    end = time.perf_counter_ns()
    print(f'Runtime: {(end-start)/1_000_000} ms')
