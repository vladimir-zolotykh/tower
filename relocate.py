#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> solve([[2, 1], [], []], 2, 0, 2)
[[], [], [2, 1]]
>>> solve([[2, 1], [], []], 2, 0, 1)
[[], [2, 1], []]
>>> solve([[], [2, 1], []], 2, 1, 2)
[[], [], [2, 1]]
>>> solve([[3, 2, 1], [], []], 3, 0, 2)
[[], [], [3, 2, 1]]
>>> solve([[3, 2, 1], [], []], 3, 0, 1)
[[], [3, 2, 1], []]
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


def solve(rods: Rods, n: int, from_rod: int, to_rod, show: bool = True):
    """Move N disks from FROM_ROD to TO_ROD"""

    if (2, 0, 2) == (n, from_rod, to_rod):
        move(rods, (0, 1), (0, 2), (1, 2))
    elif (2, 0, 1) == (n, from_rod, to_rod):
        move(rods, (0, 2), (0, 1), (2, 1))
    elif (2, 1, 2) == (n, from_rod, to_rod):
        move(rods, (1, 0), (1, 2), (0, 2))
    elif (3, 0, 2) == (n, from_rod, to_rod):
        solve(rods, 2, 0, 1, show=False)
        move(rods, (0, 2), (1, 0), (1, 2), (0, 2))
    elif (3, 0, 1) == (n, from_rod, to_rod):
        move(rods, (0, 1), (0, 2), (1, 2), (0, 1), (2, 0), (2, 1), (0, 1))
    else:
        raise ValueError("Not implemented")
    if show:
        print(rods)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
