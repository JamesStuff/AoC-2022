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

    for group_num in range(int(len(lines) / 3)):
        badge = set(lines[group_num*3]).intersection(set(lines[(group_num*3)+1]),
                                                     set(lines[(group_num*3)+2])).pop()

        if badge in string.ascii_lowercase:
            total += ord(badge) - 96

        elif badge in string.ascii_uppercase:       # Still checks to avoid edge cases of ctrl chars
            total += ord(badge) - 38

    print(total)

if __name__ == "__main__":
    main()