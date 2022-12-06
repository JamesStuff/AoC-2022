# Advent of Code 2022 - Day 06 Solution - main1.py
# Copyright James Robinson 2022
# All rights (as well as lefts) reserved.

from jimbotime import tim

n = 4


@tim.tim
def main():
    with open("input.txt") as f:
        lines = f.readlines()

    line = lines[0]

    for i in range(len(line) - n):
        flag = False
        sub = line[i:i + n]
        for s in sub:
            if sub.count(s) > 1:
                flag = True
                break

        if not flag:
            print(i + n)


if __name__ == "__main__":
    main()

