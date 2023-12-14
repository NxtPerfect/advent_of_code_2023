import time
from collections import Counter

order = {"A": 12, "K": 11, "Q": 10, "J": 9, "T": 8, "9": 7,
         "8": 6, "7": 5, "6": 4, "5": 3, "4": 2, "3": 1, "2": 0}


def run(file="input.txt"):
    total: int = 0
    totalCards: list = list()
    with open(file) as f:
        for idx, line in enumerate(f):
            cards, bet = line.strip().split(" ")
            lettersCounted: Counter = Counter(char for char in cards)
            for char in lettersCounted.most_common():
                if char[1] == 5:
                    totalCards.append(tuple((cards, int(bet), 6)))
                    break
                if char[1] == 4:
                    totalCards.append(tuple((cards, int(bet), 5)))
                    break
                if char[1] == 3 and len(lettersCounted) == 2:
                    totalCards.append(tuple((cards, int(bet), 4)))
                    break
                if char[1] == 3:
                    totalCards.append(tuple((cards, int(bet), 3)))
                    break
                if char[1] == 2 and len(lettersCounted) == 3:
                    totalCards.append(tuple((cards, int(bet), 2)))
                    break
                if char[1] == 2:
                    totalCards.append(tuple((cards, int(bet), 1)))
                    break
                if char[1] == 1:
                    totalCards.append(tuple((cards, int(bet), 0)))
                    break
            # print(totalCards)
        sorted_list = sorted(totalCards, key=lambda x: x[2], reverse=True)
        # print("Sorted list:", sorted_list)
        i = 0
        while i < len(sorted_list)-1:
            x = sorted_list[i]
            y = sorted_list[i+1]
            if x[2] != y[2]:
                i += 1
                continue
            for charX, charY in zip(x[0], y[0]):
                # print(x[0], y[0])
                # print(charX, charY)
                if order[charX] > order[charY]:
                    break
                if order[charX] == order[charY]:
                    continue
                # print("Swapping", x, y)
                temp = x
                sorted_list[i] = y
                sorted_list[i+1] = temp
                # print(sorted_list[i],
                #       sorted_list[i+1])
                i -= 2
                break
            i += 1
        # print("Hopefully sorted list:", sorted_list)
        for i, (card, bet, val) in enumerate(sorted_list):
            sorted_list[i] = (card, bet * (len(sorted_list) - i), val)
        # print(sorted_list)
    total = sum(val[1] for val in sorted_list)
    print(total)
    return total


if __name__ == "__main__":
    start = time.perf_counter_ns()
    minimum = run()
    # print(minimum == 6440) # test
    print(minimum == 6592)  # edge
    # print(minimum == 6839) # part 2
    end = time.perf_counter_ns()
    print("Runtime of " + str((end-start)/1000000) + "ms")
