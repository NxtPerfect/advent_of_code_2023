import time

# Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# For each number that we matched, we double points, first match is worth one point
# Here we matched 86, 17, 48 and 53, so it's worht 8 points (1, 2, 4, 8)
# Left is winning numbers, right is our numbers


def run(file="./input.txt"):
    total = 0
    with open(file) as f:
        for line in f:
            lineTotal = 1/2
            winningNum, ourNum = line.split("|")
            _, winningNum = winningNum.split(":")
            ourNum = " ".join(ourNum.split())
            winningNum = " ".join(winningNum.split())
            ourNum = ourNum.split(" ")
            winningNum = winningNum.split(" ")

            for x in ourNum:
                if x in winningNum:
                    lineTotal *= 2
                #     print(f'Found {x} for {lineTotal} points')
                # print(x)
            total += int(lineTotal)
    #         print(winningNum)
    #         print(ourNum)
    # print(total)
    return total


if __name__ == "__main__":
    start = time.perf_counter_ns()
    total = run()
    # print("Did we get correct number? " + str(total == 13))
    end = time.perf_counter_ns()
    print("Runtime of " + str(end-start) + "ns")
