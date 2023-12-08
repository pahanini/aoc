from utils import read_str
from re import split
from math import floor, ceil


def pzl(gg, join=False):
    if join:
        gg = [g.replace(' ', '').replace(':', ' ') for g in gg]
    tt = map(int, split(r'\s+', gg[0])[1:])
    dd = map(int, split(r'\s+', gg[1])[1:])
    r = 1
    for t, d in zip(tt, dd):
        d += 0.00000001
        D = t**2 - 4*d
        if D < 0:
            raise ValueError
        l = ceil((t - D ** 0.5) / 2)
        u = floor((t + D ** 0.5) / 2)
        r *= u - l + 1
    return r


tst = read_str('06.tst')
assert pzl(tst) == 288
assert pzl(tst, True) == 71503

dat = read_str('06.dat')
print("day 6 puzzle part 1 =", pzl(dat))
print("day 6 puzzle part 2 =", pzl(dat, True))
