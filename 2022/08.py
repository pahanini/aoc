from utils import read_str
from operator import add
from math import prod

dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]


def read(fn: str) -> dict:
    f = {}
    d = read_str(fn)
    for y, s in enumerate(d):
        for x, t in enumerate(s):
            f[(x, y)] = int(t)
    return f


def find(f, p, d) -> int:
    return max(f[p], find(f, np, d) if (np := tuple(map(add, p, dirs[d]))) in f else 0)


def is_visible(f, p) -> bool:
    return any([(np := tuple(map(add, p, dirs[d]))) not in f or f[p] > find(f, np, d) for d in range(0, len(dirs))])


def distance(f, p, d, m, c=0):
    if p not in f:
        return c
    if f[p] >= m:
        return c + 1
    else:
        return distance(f, tuple(map(add, p, dirs[d])), d, m, c + 1)


def score(f, p) -> int:
    r = []
    for d in range(0, len(dirs)):
        np = tuple(map(add, p, dirs[d]))
        r.append(distance(f, np, d, f[p]))
    return prod(r)


def pzl1(f) -> int:
    return sum([is_visible(f, p) for p in f.keys()])


def pzl2(f) -> int:
    return max([score(f, p) for p in f.keys()])


dat = read("08.tst")

assert pzl1(dat) == 21
assert pzl2(dat) == 8

dat = read("08.dat")

print("day 8 puzzle 1 =", pzl1(dat))
print("day 8 puzzle 2 =", pzl2(dat))
