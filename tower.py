#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""Tower of Hanoi"""


# Move 3 disks from rod1 to rod3 in y moves
MOVES3_1_3 = ((1, 3), (1, 2), (3, 2), (1, 3), (2, 1), (2, 3), (1, 3))
# Move 3 disks from rod1 to rod2 in 7 moves
MOVES3_1_2 = ((1, 2), (1, 3), (2, 3), (1, 2), (3, 1), (3, 2), (1, 2))
# Move 4 disks from rod1 to rod3 in 15 moves
# fmt: off
MOVES4_1_3 = (
    (1, 2), (1, 3), (2, 3), (1, 2), (3, 1), (3, 2), (1, 2),
    (1, 3), (2, 3), (2, 1), (3, 1), (2, 3), (1, 2), (1, 3), (2, 3)
)
# fmt: on


class Rod(list):
    def append(self, d):
        if not self or d < self[-1]:
            super().append(d)
        else:
            raise ValueError(f"Can't put {d} on {self[-1]}")


Tws = tuple[Rod, Rod, Rod]


def _move(rods: Tws, moves: tuple[tuple[int, int], ...]) -> Tws:
    return rods


def setup(disks: int = 3) -> None:
    rods: Tws = (Rod((3, 2, 1)), Rod(), Rod())
    res: Tws
    res = solve(rods)
    print(res)


def solve(rods: Tws) -> Tws:
    rod1: Rod = rods[0]
    res: Tws
    if len(rod1) == 1:
        return _move(rods, ((1, 3),))
    elif len(rod1) == 2:
        return _move(rods, ((1, 2), (1, 3), (2, 3)))
    elif len(rod1) == 3:
        return _move(rods, MOVES3_1_3)
    else:
        return solve(_move(rods, MOVES3_1_2))
