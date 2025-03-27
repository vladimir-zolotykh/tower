#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""Tower of Hanoi"""


class Rod(list):
    def append(self, d):
        if not self or d < self[-1]:
            super().append(d)
        else:
            raise ValueError(f"Can't put {d} on {self[-1]}")


rod1 = Rod()
rod2 = Rod()
rod3 = Rod()

for d in reversed(range(1, 4)):
    rod1.append(d)
# >>> rod1
# [2, 1]


def empty_rod3():
    """Move disks from ROD3 to ROD1"""
    move2(rod3, rod1)


def move2(rod_from: Rod, rod_to: Rod, rod_temp: Rod = rod2):
    """Move two top disks from ROD_FROM to ROD_TO"""
    d = rod_from.pop()
    rod_temp.append(d)
    rod_to.append(rod_from.pop())
    rod_to.append(rod_temp.pop())


if __name__ == "__main__":
    print(f"{rod1 = }, {rod2 = }, {rod3 = }")
    move2(rod1, rod3)
    print(f"{rod1 = }, {rod2 = }, {rod3 = }")
    empty_rod3()
    print(f"{rod1 = }, {rod2 = }, {rod3 = }")
