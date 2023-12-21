import time

# NOT OPTIMIZED
# this code works pretty badly, takes 1s for part 2


def run(file="input.txt"):
    space: list = list()
    galaxies: list = list()
    with open(file) as f:
        for idx, line in enumerate(f):
            line = line.strip()
            space.append([x for x in line])
            # Double rows
            if set(line) != set('.'):
                continue
            space.append([x for x in line])
    # Double columns
    column: list = list()
    for idc, col in enumerate(zip(*space)):
        if set(col) != set('.'):
            continue
        column.append(idc)

    # for x in space:
    #     print(x)
    for y in range(len(space)):
        insert = 0
        for c in column:
            insert += 1
            space[y].insert(c+insert, '.')
    # for x in space:
    #     print(x)

    for idx, x in enumerate(space):
        for idy, y in enumerate(x):
            if y != '#':
                continue
            galaxies.append((idx, idy))
    # print(galaxies)

    total: int = 0
    for x, y in galaxies:
        for x1, y1 in galaxies[::1]:
            total += abs(x-x1)+abs(y-y1)

    print((total//2))
    return (total//2)


def part2(file="input.txt"):
    space: list = list()
    galaxies: list = list()
    row: list = list()
    with open(file) as f:
        for idx, line in enumerate(f):
            line = line.strip()
            space.append([x for x in line])
            # Double rows
            if set(line) != set('.'):
                continue
            row.append(idx)
    # Double columns
    column: list = list()
    for idc, col in enumerate(zip(*space)):
        if set(col) != set('.'):
            continue
        column.append(idc)

    for idx, x in enumerate(space):
        for idy, y in enumerate(x):
            if y != '#':
                continue
            galaxies.append((idx, idy))
    # print(galaxies)

    cur: list = list()
    total: int = 0
    offset: int = 1000000-1
    for y, x in galaxies:
        cur.append((x, y))
        for y1, x1 in galaxies[::1]:
            # if x == x1 and y == y1:
            #     continue
            if (x1, y1) in cur:
                continue
            mult: int = 0
            # print(column, row)
            total += abs(x-x1)+abs(y-y1)
            for c in column:
                # print('P1:', x, y, 'P2:', x1, y1)
                # print('P1:', x, y, 'P2:', x1, y1, 'Mil', c, r)
                if c in range(min(x, x1), max(x, x1)):
                    mult += offset
                    # total += offset
            for r in row:
                if r in range(min(y, y1), max(y, y1)):
                    mult += offset
                    # total += offset
            total += mult
            # print("Mult:", mult, 'P1', x, y, 'P2', x1, y1)
    print(total)
    return (total)


if __name__ == "__main__":
    start = time.perf_counter_ns()
    p1 = run()
    p2 = part2()
    # print(p1 == 374)  # test
    # print(p2 == 1030)  # test part 2
    # print(p2 == 8410) # test part 2
    print(p2 not in [550189155896, 1100378311792])  # test part 2
    end = time.perf_counter_ns()
    print(f'Runtime: {(end-start)/1_000_000} ms')
