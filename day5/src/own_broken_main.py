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


def run(file="test.txt"):
    seeds = list()
    # tempSeeds = seeds.copy()
    new_ranges = list()
    conversion = [1] * 3
    with open(file) as f:
        for idx, line in enumerate(f):
            # Copy value of seeds if we run out of values to compare to
            if line == "\n" or line.find("map:") != -1:
                seeds.append(new_ranges)
                print("Append seeds")
                # tempSeeds = seeds.copy()
                continue
            # Initial run
            if idx == 0:
                _, temp = line.strip().split(":")
                # take numbers as ranges and add to seeds
                _seeds = temp.strip().split(" ")
                _seeds = list(map(int, _seeds))
                for i in range(0, len(_seeds)-1, 2):
                    seeds.append(range(_seeds[i],
                                       _seeds[i] + _seeds[i+1]))
                print(seeds)
                # tempSeeds = seeds.copy()
                continue
            # If tempSeeds was emptied, because we changed every value in list
            # if len(tempSeeds) == 0:
            #     tempSeeds = seeds.copy()
            conversion = line.strip().split(" ")
            conversion = list(map(int, conversion))
            change_range = range(conversion[1],
                                 conversion[1] + conversion[2])
            product_range = range(conversion[0],
                                  conversion[0] + conversion[1])
            print("Line:", conversion)
            # prodStart, sourceStart, length = map(int, conversion)
            # Iterate over seeds to change their values, if they're in tempSeeds, that means they weren't changed
            for idx, seed in enumerate(seeds):
                intersection_start = max(seed.start, change_range.start)
                intersection_stop = max(seed.stop, change_range.stop)
                if intersection_start > intersection_stop:
                    continue
                new_ranges.append(
                    range(product_range.start, product_range.stop))
                print("New ranges: ", new_ranges)
                seeds[idx] = range(seed.start, intersection_start)
                print("Creating tuple?",
                      seeds[idx+1], type(seeds[idx+1]), seed.start, intersection_start)
            print(seeds)
            print(new_ranges)
            # print(tempSeeds)
        # print(min(seeds))
        # return min(seeds)


if __name__ == "__main__":
    start = time.perf_counter_ns()
    minimum = run()
    # print("Is it correct?", minimum == 35)
    print("Is it correct?", minimum == 46)
    end = time.perf_counter_ns()
    print("Runtime of " + str((end-start)/1000000) + "ms")
