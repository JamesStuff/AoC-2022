# Advent of Code 2022 - Day 04 Solution - main1.py
# Copyright James Robinson 2022
# All rights (as well as lefts) reserved.

from jimbotime import tim


@tim.tim
def main():
    with open("input.txt") as f:
        lines = f.readlines()

    print(len(lines))

    count = 0

    for entry in lines:
        entry = entry.replace("\n", "").split(",")

        a, b = entry
        a, b = a.split("-"), b.split("-")
        a, b = [int(i) for i in a], [int(i) for i in b]

        if (a[1] >= b[0] and a[0] <= b[1]) and (b[1] >= a[0] and b[0] <= a[1]):
            print(entry, "\ta, b:",a, b)
            count += 1

    print(count)
    print("923 is too high...")


if __name__ == "__main__":
    main()
