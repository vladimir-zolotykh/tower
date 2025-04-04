#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""
>>> move3_0_2([Rod([3, 2, 1]), Rod(), Rod()])
[[], [], [3, 2, 1]]
>>> move3_0_1([Rod([3, 2, 1]), Rod(), Rod()])
[[], [3, 2, 1], []]
>>> move3_1_2([Rod(), Rod([3, 2, 1]), Rod()])
[[], [], [3, 2, 1]]
>>> solve([Rod([3, 2, 1]), Rod(), Rod()])
[[], [], [3, 2, 1]]
>>> move4_0_1(([Rod([4, 3, 2, 1]), Rod(), Rod()]))
[[], [], [4, 3, 2, 1]]
>>> solve([Rod([4, 3, 2, 1]), Rod(), Rod()])
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


def move(rods: Rods, *moves: tuple[int, int]) -> Rods:
    for move in moves:
        assert move[0] != move[1]
        disk = rods[move[0]].pop()
        rods[move[1]].append(disk)
    return rods


def move3_0_2(rods: Rods) -> Rods:
    """Move 3 top disks from ROD0 to ROD2"""

    move(rods, (0, 2), (0, 1), (2, 1), (0, 2), (1, 0), (1, 2), (0, 2))
    return rods


def move3_0_1(rods: Rods) -> Rods:
    """Move 3 top disk from ROD0 to ROD1"""

    move(rods, (0, 1), (0, 2), (1, 2), (0, 1), (2, 0), (2, 1), (0, 1))
    return rods


def move3_1_2(rods: Rods) -> Rods:
    """Move 3 top disks from ROD1 to ROD2"""

    move(rods, (1, 2), (1, 0), (2, 0), (1, 2), (0, 1), (0, 2), (1, 2))
    return rods


def move4_0_1(rods: Rods) -> Rods:
    move3_0_1(rods)
    move(rods, (0, 2))
    move3_1_2(rods)
    return rods


def move4_1_2(rods: Rods) -> Rods:
    pass


def solve(rods: Rods) -> Rods:
    if len(rods[0]) == 3:
        move3_0_2(rods)
    elif len(rods[0]) == 4:
        move4_0_1(rods)
        # move3_0_1(rods)
        # move(rods, (0, 2))
        # move3_1_2(rods)
    elif len(rods[0]) == 5:
        move4_0_1(rods)
        move(rods, (0, 2))
        move4_1_2(rods)
    else:
        raise ValueError("Not implemented yet")
    return rods


if __name__ == "__main__":
    import doctest

    doctest.testmod()
