from utils import read_groups
from functools import cmp_to_key
from math import prod


def read(f: str):
    return [list(map(eval, g)) for g in read_groups(f)]


def cmp(a, b):
    match a, b:
        case int(), int():
            return (a > b) - (a < b)
        case int(), list():
            return cmp([a], b)
        case list(), int():
            return cmp(a, [b])
        case list(), list():
            for a0, b0 in zip(a, b):
                if t := cmp(a0, b0):
                    return t
            return cmp(len(a), len(b))


def pzl1(gg):
    return sum(i for i, (a, b) in enumerate(gg, 1) if cmp(a, b) == -1)


def pzl2(gg):
    dd = [[2], [6]]
    t = []
    for (a, b) in gg:
        t += [a, b]
    t = sorted(t + dd, key=cmp_to_key(cmp))
    return prod([t.index(d) + 1 for d in dd])


dat = read('13.tst')

assert pzl1(dat) == 13
assert pzl2(dat) == 140

dat = read('13.dat')

print("day 13 puzzle 1 =", pzl1(dat))
print("day 12 puzzle 2 =", pzl2(dat))
