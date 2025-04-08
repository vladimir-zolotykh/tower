#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> solve([[3, 2, 1], [], []], 3, 0, 2)
[[], [], [3, 2, 1]]
>>> solve([[4, 3, 2, 1], [], []], 4, 0, 2)
[[], [], [4, 3, 2, 1]]
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
rods: Rods = []


def move(rods: Rods, *moves: tuple[int, int]):
    for move in moves:
        assert move[0] != move[1]
        disk = rods[move[0]].pop()
        rods[move[1]].append(disk)
    return rods


def solve(rods: Rods, n: int, i: int, j: int) -> None:
    t: int = set(range(3)) - set([i, j])  # temporary rod
    if n == 1:
        move(rods, i, j)
    elif n == 2:
        move(rods, (i, t), (i, j), (t, j))
    if n == 3:
        solve(rods, n - 1, i, t, show=False)
        move(rods, (i, j))
        solve(rods, n - 1, t, j, show=False)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
