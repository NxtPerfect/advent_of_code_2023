from collections import defaultdict
import unittest


class TestAdvent(unittest.TestCase):
    def test(self):
        self.assertEqual(run("./test.txt"), 81)


lookup = {"one": 1, "two": 2, "three": 3, "four": 4,
          "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def run(file='./input.txt'):
    file = open(file, 'r')
    lines = file.readlines()
    res = defaultdict(tuple)
    summ = 0

    for i, line in enumerate(lines):
        left = -1
        right = -1
        leftpos = -1
        rightpos = -1
        for j, ch in enumerate(line):
            if left != -1 and ch.isnumeric():
                right = ch
                rightpos = j
            if left == -1 and ch.isnumeric():
                left = ch
                leftpos = j
                right = ch
                rightpos = j

        for key in lookup.keys():
            if key not in line:
                continue

            lastpos = 0
            # for word in lookup:
            while lastpos != -1:
                curpos = line.find(key, lastpos)
                if curpos == -1:
                    break
                if curpos < leftpos or leftpos == -1:
                    left = lookup.get(key)
                    leftpos = curpos
                if curpos > rightpos:
                    right = lookup.get(key)
                    rightpos = curpos
                lastpos = curpos + 1

        res[i] = (left, right)
        summ += int(res[i][0]) * 10 + int(res[i][1])
    print(summ)
    return summ


if __name__ == "__main__":
    run()
    # unittest.main()
