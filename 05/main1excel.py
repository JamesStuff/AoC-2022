# Advent of Code 2022 - Day XX Solution - main1.py
# Copyright James Robinson 2022
# All rights (as well as lefts) reserved.

from time import sleep

from pynput.keyboard import Controller as KController
from pynput.keyboard import Key
from pynput.mouse import Controller as MController
from tqdm import tqdm

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

keyboard = KController()
mouse = MController()


def dt(t=0.1): sleep(t)


def type_delay(s):
    for c in s:
        keyboard.type(c)
        dt()


def select_column_top(num):
    keyboard.press(Key.cmd)
    keyboard.press(Key.up)
    dt()
    keyboard.release(Key.up)
    keyboard.press(Key.left)
    dt()
    keyboard.release(Key.left)

    keyboard.release(Key.cmd)

    for _ in range(num):
        keyboard.press(Key.right)
        dt()
        keyboard.release(Key.right)


def cmd_plus(plus):
    keyboard.press(Key.cmd)
    keyboard.press(plus)
    dt()
    keyboard.release(plus)
    keyboard.release(Key.cmd)


def mcro():
    keyboard.press(Key.cmd)
    keyboard.press(Key.alt)
    keyboard.press("b")
    dt()
    dt()
    keyboard.release("b")
    keyboard.press(Key.alt)
    keyboard.release(Key.cmd)


def move_down():
    cmd_plus(Key.down)


def cut():
    cmd_plus("x")


def paste():
    keyboard.press(Key.up)
    dt()
    keyboard.release(Key.up)

    cmd_plus("v")


@tim.tim
def main():
    with open("input.txt") as f:
        lines = f.readlines()

    print(len(lines))

    for line in tqdm(lines):
        line = line.replace("move ", "") \
            .replace("from ", "") \
            .replace("to ", "") \
            .replace("\n", "") \
            .split(" ")
        int_line = [int(i) for i in line]

        for _ in range(int_line[0]):
            select_column_top(int_line[1])
            move_down()
            cut()

            select_column_top(int_line[2])
            move_down()
            paste()


if __name__ == "__main__":
    for i in range(3):
        print(3 - i, "...", sep="")
        sleep(1)

    main()
