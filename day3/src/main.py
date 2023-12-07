from collections import defaultdict


# ......755.
# ...$.*....
# .664.598..
# Gear ratio is calculated by multiplying two numbers that both touch the same symbol
# Then i need to sum them all up


def run(file='./input.txt'):
    total = 0
    gears = 0
    symbols_in_line, stars_in_line = list(), list()
    symbols, stars, digits = defaultdict(
        list), defaultdict(list), defaultdict(list)
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

    # Part one
    for line in lines:
        for char in range(len(line)):
            if line[char].isdigit() or line[char] == '.' or line[char] == '\n' or line[char] == ' ':
                continue
            if line[char] == '*':
                stars_in_line.append(char)
            symbols_in_line.append(char)
        stars[lines.index(line)] = stars_in_line
        stars_in_line = list()
        symbols[lines.index(line)] = symbols_in_line
        symbols_in_line = list()

    print(symbols.values())
    for row, column in symbols.items():
        # print(column)
        for i, x in enumerate(column):
            # print(x)
            for t in [-1, 0, 1]:
                # print(
                #     f'Iteration {i+t} for column {row}, with numbers {digits[row+t]}')
                a = row + t
                if a < 0 or a >= len(digits):
                    continue
                for y in digits[a]:
                    start = y[0]-1
                    if y[0] == 0:
                        start = y[0]
                    if x not in range(start, y[0] + len(y[1])+1):
                        # print("not found")
                        continue
                    # print(f'{y[1]} found for col {row}')
                    total += int(y[1])

    # Part two
    for row, column in stars.items():
        print(column)
        for x in column:
            print(x)
            gearratio = 0
            one, two = False, False
            for t in [-1, 0, 1]:
                a = row + t
                if a < 0 or a >= len(digits):
                    continue
                for y in digits[a]:
                    start = y[0] - 1
                    if y[0] == 0:
                        start = y[0]
                    if x not in range(start, y[0] + len(y[1])+1):
                        continue
                    print(f'Found {y[1]}')
                    print(f'Ratio: {gearratio}')
                    if not one:
                        gearratio = int(y[1])
                        one = True
                        continue
                    if one and two:
                        gearratio = 0
                        continue
                    if one:
                        gearratio *= int(y[1])
                        two = True
            print(f'Gears col: {gears}')
            if not two:
                gearratio = 0
            gears += gearratio

    print("Total: " + str(total))
    print("Gears: " + str(gears))
    return total


if __name__ == "__main__":
    run()
