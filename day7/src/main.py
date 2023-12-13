import time
from collections import Counter

# sequences of cards into points
# then each card into individual point if not in any sequence
# change them into dict?

# Order: A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, 2

order = {"A": 0, "K": 1, "Q": 2, "J": 3, "T": 4, "9": 5,
         "8": 6, "7": 7, "6": 8, "5": 9, "4": 10, "3": 11, "2": 12}


def customOrder(item: dict):
    max_value: int = max(item[0].values())
    custom_key: tuple = tuple(order.get(key, float('inf'))
                              for key in item[0])
    return (-max_value, custom_key)


def run(file="edge.txt"):
    total = 0
    cardsInGames: dict = dict()
    with open(file) as f:
        for idx, line in enumerate(f):
            cards, bet = line.strip().split(" ")
            lettersCounted: Counter = Counter(char for char in cards)
            cardsCounted: dict = dict(lettersCounted.most_common())
            # print(cardsCounted.items())
            cardsInGames[idx+1] = tuple((cardsCounted, int(bet)))
        # print(cardsInGames.items())
        # rankedGames: dict = dict(sorted(cardsInGames.items(),
        #                                 key=lambda x: max(x[1].values()), reverse=False))
        # print(cardsInGames.items())
        # rankedGames: dict = {idx: val for idx, val in enumerate(
        #     sorted(cardsInGames.values(), key=customOrder))}
        rankedGames: dict = {k: v for k, v in sorted(
            cardsInGames.items(), key=lambda x: customOrder(x[1]))}
        # print("Before multiplying bids\n", rankedGames)
        for i, (key, (inner_dict, val)) in enumerate(rankedGames.items()):
            rankedGames[key] = (inner_dict, val*(len(rankedGames) - i))
        # print("After multiplying bids\n", rankedGames)

        print(cardsInGames.items())
    total = sum(val[1] for val in rankedGames.values())
    print(total)
    return total


if __name__ == "__main__":
    start = time.perf_counter_ns()
    minimum = run()
    # print(minimum == 6440)
    print(minimum == 6592)
    end = time.perf_counter_ns()
    print("Runtime of " + str((end-start)/1000000) + "ms")
