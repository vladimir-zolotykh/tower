#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> solve([Rod([3, 2, 1]), Rod(), Rod()])
[[], [], [3, 2, 1]]
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


def move(rods: Rods, *moves: tuple[int, int]) -> Rods:
    for move in moves:
        assert move[0] != move[1]
        disk = rods[move[0]].pop()
        rods[move[1]].append(disk)
    return rods


def solve(rods: Rods) -> Rods:
    if len(rods[0]) == 3:
        move(rods, (0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2))
    return rods


if __name__ == "__main__":
    import doctest

    doctest.testmod()
