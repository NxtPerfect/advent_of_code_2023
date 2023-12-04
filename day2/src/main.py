def run():
    # Game N: 3 X, 4 Y, 5Z; 2X\n
    total = 0
    with open("./input.txt") as f:
        for line in f:
            red, green, blue = 0, 0, 0
            left, games = line.split(": ")
            _, gameid = left.split(" ")
            if gameid is None:
                gameid = 0
            game = games.split(";")
            print(f'{line}')
            for cube in game:
                cubes = cube.split(",")
                print(cubes)
                for c in cubes:
                    c = c.strip()
                    num, col = c.split(" ")
                    if col == "red" and int(num) > red:
                        red = int(num)
                        continue
                    if col == "green" and int(num) > green:
                        green = int(num)
                        continue
                    if col == "blue" and int(num) > blue:
                        blue = int(num)
                        continue
            if red > 12 or green > 13 or blue > 14:
                continue
            print(gameid)
            total += int(gameid)
    print(total)


if __name__ == "__main__":
    run()
