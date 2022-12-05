# Advent of Code 2022 - Day 02 Solution - main2.py
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
    score = 0
    with open("input.txt") as f:
        lines = f.readlines()

    print(len(lines))

    for l in lines:
        moves = l.replace("\n", "").split(" ")

        if moves[1] == "X":
            score += 0
        elif moves[1] == "Y":
            score += 3
        elif moves[1] == "Z":
            score += 6

        if moves[0] == "A":
            if moves[1] == "X":
                score += 3
            elif moves[1] == "Y":
                score += 1
            else:
                score += 2

        elif moves[0] == "B":
            if moves[1] == "X":
                score += 1
            elif moves[1] == "Y":
                score += 2
            else:
                score += 3

        else:
            if moves[1] == "X":
                score += 2
            elif moves[1] == "Y":
                score += 3
            else:
                score += 1

    return score


if __name__ == "__main__":
    score = main()

    print(score)
