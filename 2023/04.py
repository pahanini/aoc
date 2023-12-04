from utils import read_str
import re
from math import pow


def pzl(ll, ws=10):
    r0 = 0
    r1 = [1] * len(ll)
    for i, l in enumerate(ll):
        t = re.split(r'\s+', l)
        w = set([int(v) for v in t[2: 2+ws]])
        h = set([int(v) for v in t[3+ws:]])
        g = len(w & h)
        for v in range(i, i+g):
            r1[v + 1] += 1 * r1[i]
        if g:
            r0 += pow(2, g - 1)
    return r0, sum(r1)


tst = read_str('04.tst')
assert pzl(tst, ws=5) == (13, 30)

dat = read_str('04.dat')

print("day 4 puzzle =", pzl(dat))
