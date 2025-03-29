#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
"""Tower of Hanoi"""
import copy

# Move 3 disks from rod1 to rod3 in y moves
MOVES3_1_3 = ((1, 3), (1, 2), (3, 2), (1, 3), (2, 1), (2, 3), (1, 3))
# Move 3 disks from rod1 to rod2 in 7 moves
MOVES3_1_2 = ((1, 2), (1, 3), (2, 3), (1, 2), (3, 1), (3, 2), (1, 2))
# Move 3 disks from rod2 to rod3 in 7 moves
MOVES3_2_3 = ((2, 3), (2, 1), (3, 1), (2, 3), (1, 2), (1, 3))
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
    # rods = copy.copy(rods)
    for move in moves:
        from_, to_ = move
        x = rods[from_ - 1].pop()
        rods[to_ - 1].append(x)
    return rods


def setup(disks: int = 3) -> Tws:
    return (Rod((3, 2, 1)), Rod(), Rod())


def solve(rods: Tws) -> Tws:
    rod1: Rod = rods[0]
    if len(rod1) == 1:
        return _move(rods, ((1, 3),))
    elif len(rod1) == 2:
        return _move(rods, ((1, 2), (1, 3), (2, 3)))
    elif len(rod1) == 3:
        return _move(rods, MOVES3_1_3)
    else:
        res = _move(rods, MOVES3_1_2)
        res = _move(res, ((1, 3),))
        return solve(_move(res, MOVES3_2_3))


if __name__ == "__main__":
    rods: Tws = setup(3)
    print(f"0 {rods = }")
    res: Tws = solve(rods)
    print(f"1 {res = }")
