#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# PYTHON_ARGCOMPLETE_OK
from typing import Optional, Any, SupportsIndex
import unittest


class Rod(list):
    def append(self, d):
        if not self or d < self[-1]:
            super().append(d)
        else:
            raise ValueError(f"Can't put larger {d} on smaller {self[-1]}")

    def pop(self, index: SupportsIndex = -1) -> Any:
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


# fmt: off
def solve(
        n: int, i: int, j: int, rods0: Rods | None = None
) -> Optional[tuple[Rods, int]]:
    # fmt: on
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
    else:
        return None


class TowerTest(unittest.TestCase):
    max_disks: int = 8

    def setUp(self, *args, **kw) -> None:
        super().setUp(*args, **kw)
        print()

    def test_towers(self) -> None:
        for n in range(3, self.max_disks + 1):
            global rods
            rods0: Rods = make_rods0(n)
            print(f"Testing {n} disks")
            solve(n, 0, 2, rods0=rods0)
            self.assertEqual(rods, rods0)


if __name__ == "__main__":
    TowerTest.max_disks = 8
    unittest.main(verbosity=2)
