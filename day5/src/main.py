import time

# First we have the destination range start -> 50/52, then we have source range start -> 98/50
# and then the length of that range -> 2/48
# We have to find the **lowest** location number -> number after all the conversions
# seed-to-soil map:
# 50 98 2
# 52 50 48

# Store values in a set because you only can store unique entries, and it's sorted
# Use two sets, one is more persistent, only holding full data once we encounter empty \n line
# Another is temporary, holding values between conversions


def run(file="input.txt"):
    seeds = [1] * 20
    tempSeeds = seeds.copy()
    conversion = [1] * 3
    with open(file) as f:
        for idx, line in enumerate(f):
            # Copy value of seeds if we run out of values to compare to
            if line == "\n" or line.find("map:") != -1:
                tempSeeds = seeds.copy()
                continue
            # Initial run
            if idx == 0:
                _, seeds = line.strip().split(":")
                seeds = map(int, seeds.strip().split(" "))
                seeds = list(seeds)
                tempSeeds = seeds.copy()
                continue
            # If tempSeeds was emptied, because we changed every value in list
            if len(tempSeeds) == 0:
                tempSeeds = seeds.copy()
            conversion = line.strip().split(" ")
            print("Line:", conversion)
            prodStart, sourceStart, length = map(int, conversion)
            # Iterate over seeds to change their values, if they're in tempSeeds, that means they weren't changed
            for idx, seed in enumerate(seeds):
                if len(tempSeeds) == 0:
                    break
                if seed not in tempSeeds:
                    continue
                if seed not in range(sourceStart, sourceStart+length):
                    continue
                seeds[idx] = prodStart + abs(seed - sourceStart)
                tempSeeds.pop(tempSeeds.index(seed))
            # seeds = [prodStart + abs(seed - sourceStart) if seed in range(
            #     sourceStart, sourceStart + length) else seed for seed in seeds]
            print(seeds)
            print(tempSeeds)
        print(min(seeds))
        return min(seeds)


if __name__ == "__main__":
    start = time.perf_counter_ns()
    minimum = run()
    print("Is it correct?", minimum == 35)
    end = time.perf_counter_ns()
    print("Runtime of " + str((end-start)/1000000) + "ms")
