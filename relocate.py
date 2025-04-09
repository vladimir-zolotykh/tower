#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> print(solve(3, 0, 2, rods0 = make_rods0(3)))
([[], [], [3, 2, 1]], 7)
>>> print(solve(4, 0, 2, rods0 = make_rods0(4)))
([[], [], [4, 3, 2, 1]], 15)
>>> print(solve(5, 0, 2, rods0 = make_rods0(5)))
([[], [], [5, 4, 3, 2, 1]], 31)
>>> print(solve(6, 0, 2, rods0 = make_rods0(6)))
([[], [], [6, 5, 4, 3, 2, 1]], 63)
>>> print(solve(7, 0, 2, rods0 = make_rods0(7)))
([[], [], [7, 6, 5, 4, 3, 2, 1]], 127)
>>> print(solve(8, 0, 2, rods0 = make_rods0(8)))
([[], [], [8, 7, 6, 5, 4, 3, 2, 1]], 255)
"""

from typing import Any


class Rod(list):
    def append(self, d):
        if not self or d < self[-1]:
            super().append(d)
        else:
            raise ValueError(f"Can't put larger {d} on smaller {self[-1]}")

    def pop(self, index: int = -1) -> Any:
        if index != -1:
            raise ValueError("Can POP only the last element of the list")
        else:
            return super().pop()


Rods = list[Rod]
rods: Rods
count: int = 0  # total moves


def move(*moves: tuple[int, int]) -> None:
    global rods
    global count
    for move in moves:
        assert move[0] != move[1]
        disk = rods[move[0]].pop()
        rods[move[1]].append(disk)
        count += 1


def make_rods0(n: int) -> Rods:
    return [Rod(range(n, 0, -1)), Rod(), Rod()]


def solve(n: int, i: int, j: int, rods0: Rods | None = None) -> None:
    global rods
    global count
    if rods0:
        rods = rods0
        count = 0
    t: int = (set(range(3)) - set([i, j])).pop()
    if n == 1:
        move((i, j))
    elif n == 2:
        move((i, t), (i, j), (t, j))
    if 3 <= n:
        solve(n - 1, i, t)
        move((i, j))
        solve(n - 1, t, j)
    if rods0:
        return rods, count


if __name__ == "__main__":
    import doctest

    doctest.testmod()
