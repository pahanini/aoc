from utils import read_str
from collections import defaultdict
from math import prod
import re


def pzl(gg):
    r1 = r2 = 0
    for g in gg:
        d = re.sub("[,;:]", "", g).split()
        cmax = defaultdict(int)
        for i in range(2, len(d), 2):
            cmax[d[i+1]] = max(cmax[d[i+1]], int(d[i]))
        if cmax['red'] <= 12 and cmax['green'] <= 13 and cmax['blue'] <= 14:
            r1 += int(d[1])
        r2 += prod(cmax.values())
    return r1, r2


tst = read_str('02.tst')

assert pzl(tst) == (8, 2286)

dat = read_str('02.dat')

print("day 2 puzzle =", pzl(dat))
