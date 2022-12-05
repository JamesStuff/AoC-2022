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

        if ((int(a[0]) <= int(b[0])) and (int(a[1]) >= int(b[1]))) or \
                ((int(b[0]) <= int(a[0])) and (int(b[1]) >= int(a[1]))):
            print("a, b:",a, b)
            count += 1

    print(count)
    print("507 is too high...")


if __name__ == "__main__":
    main()
