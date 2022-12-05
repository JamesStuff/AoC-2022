# Advent of Code 2022 - Day 03 Solution - main1.py
# Copyright James Robinson 2022
# All rights (as well as lefts) reserved.

import string
from jimbotime import tim

@tim.tim
def main():
    with open("input.txt") as f:
        lines = f.readlines()


    total = 0
    lines = [i.replace("\n", "") for i in lines]

    for l in lines:
        a = l[:int(len(l)/2)]
        b = l[int(len(l)/2):]

        for c in a:
            if c in b:
                if c in string.ascii_lowercase:
                    total += ord(c) - 96
                elif c in string.ascii_uppercase:
                    total += ord(c) - 38

                break

    print(total)


if __name__ == "__main__":
    main()