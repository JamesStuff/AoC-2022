# Advent of Code 2022 - Day 05 Solution - main2.py
# Copyright James Robinson 2022
# All rights (as well as lefts) reserved.

from jimbotime import tim

# [N] [G]                     [Q]
# [H] [B]         [B] [R]     [H]
# [S] [N]     [Q] [M] [T]     [Z]
# [J] [T]     [R] [V] [H]     [R] [S]
# [F] [Q]     [W] [T] [V] [J] [V] [M]
# [W] [P] [V] [S] [F] [B] [Q] [J] [H]
# [T] [R] [Q] [B] [D] [D] [B] [N] [N]
# [D] [H] [L] [N] [N] [M] [D] [D] [B]
#  1   2   3   4   5   6   7   8   9

stack = [
    ["D", "T", "W", "F", "J", "S", "H", "N"],
    ["H", "R", "P", "Q", "T", "N", "B", "G"],
    ["L", "Q", "V"],
    ["N", "B", "S", "W", "R", "Q"],
    ["N", "D", "F", "T", "V", "M", "B"],
    ["M", "D", "B", "V", "H", "T", "R"],
    ["D", "B", "Q", "J"],
    ["D", "N", "J", "V", "R", "Z", "H", "Q"],
    ["B", "N", "H", "M", "S"]
]


def print2d(arr):  print('\n'.join(' '.join(str(x) for x in row) for row in arr))


@tim.tim
def main():
    with open("input.txt") as f:
        lines = f.readlines()

    print(len(lines))

    for line in lines:
        line = line.replace("move ", "").replace("from ", "").replace("to ", "").replace("\n", "").split(" ")
        int_line = [int(i) for i in line]

        t = stack[int_line[1] - 1][len(stack[int_line[1] - 1]) - int_line[0]:]

        for j in t:
            stack[int_line[2] - 1].append(j)
            stack[int_line[1] - 1].pop()

    for s in stack:
        print(s.pop(), end="")


if __name__ == "__main__":
    main()