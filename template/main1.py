# Advent of Code 2022 - Day XX Solution - main1.py
# Copyright James Robinson 2022
# All rights (as well as lefts) reserved.

from jimbotime import tim


@tim.tim
def main():
    with open("input.txt") as f:
        lines = f.readlines()

    print(len(lines))


if __name__ == "__main__":
    main()
