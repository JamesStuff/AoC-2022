# Advent of Code 2022 - Day 01 Solution - main.py
# Copyright James Robinson 2022
# All rights (as well as lefts) reserved.

from jimbotime import tim

@tim.tim
def main():
    running, top_n = 0, 0
    elves = []
    n = 3

    with open("input.txt") as f:
        for line in f:
            if line == "\n":
                elves.append(running)
                running = 0
            else:
                running += int(line)

        if running != 0: elves.append(running)

    elves.sort()
    top_n = sum(elves[len(elves) - n:])

    return n, top_n, elves


if __name__ == "__main__":
    n, top_n, elves = main()

    print(f"Total of {len(elves)} elves\nwith max of {max(elves)} cal")
    print(f"Top {n} elves are carrying {top_n} cal")
