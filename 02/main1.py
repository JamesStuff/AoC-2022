# Advent of Code 2022 - Day 02 Solution - main.py
# Copyright James Robinson 2022
# All rights (as well as lefts) reserved.

# A for Rock,
# B for Paper,
# C for Scissors

# X for Rock,
# Y for Paper,
# Z for Scissors.

# 1 for Rock,
# 2 for Paper,
# 3 for Scissors

# 0 if you lost,
# 3 if the round was a draw,
# 6 if you won

# X means you need to lose,
# Y means you need to end the round in a draw,
# Z means you need to win.

from jimbotime import tim


@tim.tim
def main():
    with open("input.txt") as f:
        lines = f.readlines()

    score = 0

    for l in lines:
        moves = l.replace("\n", "").split(" ")

        score += ord(moves[1]) - 87

        if ord(moves[0]) - 65 == ord(moves[1]) - 88:
            score += 3

        if moves[0] == "A":
            if moves[1] == "Y":
                score += 6

        if moves[0] == "B":
            if moves[1] == "Z":
                score += 6

        if moves[0] == "C":
            if moves[1] == "X":
                score += 6

    print(score)


if __name__ == "__main__":
    main()
