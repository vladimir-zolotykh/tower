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

for d in reversed(range(1, 3)):
    rod1.append(d)
# >>> rod1
# [2, 1]


def move2():
    d = rod1.pop()
    rod2.append(d)
    rod3.append(rod1.pop())
    rod3.append(rod2.pop())


if __name__ == "__main__":
    print(f"{rod1 = }, {rod2 = }, {rod3 = }")
    move2()
    print(f"{rod1 = }, {rod2 = }, {rod3 = }")
