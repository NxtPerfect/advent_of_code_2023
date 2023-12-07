from collections import defaultdict

# We got the symbols
# Now if we can somehow save the numbers into list, and their starting position, we can find
# which number touches the symbol by adding length to position, and if it's same or more than
# the symbol, we're good, if starting position -1 is symbol, we're also good

# Go two lines at a time, if we find symbol, then go back one and forward one, if there's a number, add it
# 467..114..
# ...*......


def run(file='./input.txt'):
    total = 0
    symbols_in_line = list()
    symbols, digits = defaultdict(list), defaultdict(list)
    f = open(file)
    lines = f.readlines()
    for line in lines:
        temp = ""
        start = -1
        for char in range(len(line)):
            if line[char].isdigit():
                if start == -1:
                    start = char
                temp += line[char]
                continue
            if len(temp) > 0:
                digits[lines.index(line)].append((start, temp))
                temp = ""
                start = -1
            # print(digits.values())

    for line in lines:
        for char in range(len(line)):
            if line[char].isdigit() or line[char] == '.' or line[char] == '\n' or line[char] == ' ':
                continue
            # I Need to find the digits, so that i get starting point of them
            # and the whole number
            symbols_in_line.append(char)
            # print(symbols_in_line)
        symbols[lines.index(line)] = symbols_in_line
        # print(symbols.values())
        symbols_in_line = list()

    print(symbols.values())
    for row, column in symbols.items():
        print(column)

        for i, x in enumerate(column):
            for t in [-1, 0, 1]:
                print(
                    f'Iteration {i+t} for column {row}, with numbers {digits[row+t]}')
                a = row + t
                if a < 0 or a >= len(digits):
                    continue
                for y in digits[a]:
                    start = y[0]-1
                    if y[0] == 0:
                        start = y[0]
                    if x not in range(start, y[0] + len(y[1])+1):
                        print("not found")
                        continue
                    print(f'{y[1]} found for col {row}')
                    total += int(y[1])

    print(total)
    return total


if __name__ == "__main__":
    print("Did i get correct reults? " + str(run() == 4361))
    print("Should be 4361")
