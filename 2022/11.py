from utils import read_all
from collections import deque
from math import prod, lcm

import re


class Mnk:

    lcm = None
    div = 3
    all = []

    def __init__(self, st, op, dv, p1, p2):
        self.st = st
        self.wl = None
        self.cnt = 0
        self.op = op
        self.dv = dv
        self.p1 = p1
        self.p2 = p2
        self.reset()

    def reset(self):
        self.cnt = 0
        self.wl = deque(self.st)

    def turn(self):
        while len(self.wl):
            wl, n = self.inspect()
            self.all[n].wl.append(wl)

    def inspect(self) -> (int, int):
        old = self.wl.popleft()
        new = eval(self.op)
        new = new if Mnk.lcm is None else new % Mnk.lcm
        new = new if Mnk.div is None else new // Mnk.div
        self.cnt += 1
        return new, self.p1 if new % self.dv == 0 else self.p2


def read(f: str):
    mm = []
    regex = r'([0-9, ]+)\n .+=(.+)\n\D+(\d+)\n\D+(\d+)\n\D+(\d+)'
    for d in read_all(f).split("\n\n"):
        g = re.findall(regex, d, re.MULTILINE)[0]
        mm.append(Mnk(
            [int(x.strip()) for x in g[0].split(",")],
            g[1].strip(),
            *map(int, g[2:])
        ))
    Mnk.lcm = lcm(*[m.dv for m in mm])
    Mnk.all = mm
    return mm


def pzl(mm, n, div) -> int:
    for m in mm:
        m.reset()
    for i in range(0, n):
        Mnk.div = div
        for m in mm:
            m.turn()
    return prod(sorted([m.cnt for m in mm])[-2:])


dat = read("11.tst")
assert pzl(dat, 20, 3) == 10605
assert pzl(dat, 10_000, None) == 2_713_310_158

dat = read("11.dat")
print("day 11 puzzle 1 =", pzl(dat, 20, 3))
print("day 11 puzzle 2 =", pzl(dat, 10_000, None))
