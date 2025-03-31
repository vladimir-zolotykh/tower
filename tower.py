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
MOVES4_1_3 = (*MOVES3_1_2, (1, 3), *MOVES3_2_3, (2, 3))


class Rod(list):
    def append(self, d):
        if not self or d < self[-1]:
            super().append(d)
        else:
            raise ValueError(f"Can't put {d} on {self[-1]}")


Tws = tuple[Rod, Rod, Rod]  # towers


def _move(rods: Tws, moves: tuple[tuple[int, int], ...]) -> Tws:
    # rods = copy.copy(rods)
    for move in moves:
        from_, to_ = move
        x = rods[from_ - 1].pop()
        rods[to_ - 1].append(x)
    return rods


def setup(disks: int = 3) -> Tws:
    return (Rod(reversed(range(1, disks + 1))), Rod(), Rod())


Peg = Rod
Pegs = Tws


def solve2(pegs: Pegs) -> Pegs:
    peg1: Peg = pegs[0]
    if len(peg1) == 1:
        return _move(pegs, ((1, 3),))
    elif len(peg1) == 2:
        return _move(pegs, ((1, 2), (1, 3), (2, 3)))
    elif len(peg1) == 3:
        return _move(pegs, MOVES3_1_3)
    else:
        d: int = pegs[0][0]  # Biggest disk
        t: Pegs = solve2([pegs[0][1:], pegs[1], pegs[2]])
        return solve2([[d, *t[0]], t[1], t[2]])


def solve(rods: Tws) -> Tws:
    rod1: Rod = rods[0]
    if len(rod1) == 1:
        return _move(rods, ((1, 3),))
    elif len(rod1) == 2:
        return _move(rods, ((1, 2), (1, 3), (2, 3)))
    elif len(rod1) == 3:
        return _move(rods, MOVES3_1_3)
    else:
        return _move(rods, MOVES4_1_3)


if __name__ == "__main__":
    res: Tws = solve2(setup(3))
    print(f"3 disks: {res = }")
    res = solve2(setup(4))
    print(f"4 disks: {res = }")
