from utils import read_str
from math import prod
import re


dd = (-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)


def pzl(ll):
    gg = dict()
    r0 = r1 = 0
    for y, l in enumerate(ll):
        for x, c in enumerate(l):
            if c != '.' and not c.isdigit():
                gg[(x, y)] = [] if c == '*' else None

    def chk(m):
        a, b = m.span()
        for x in range(a, b):
            for d in dd:
                k = (x + d[0], y + d[1])
                if k in gg:
                    t = int(m.group())
                    if gg[k] is not None:
                        gg[k].append(t)
                    return t
        return 0

    for y, l in enumerate(ll):
        for m in re.finditer(r'(\d+)', l):
            r0 += chk(m)

    for g in gg.values():
        if g is not None and len(g) == 2:
            r1 += prod(g)

    return r0, r1


tst = read_str('03.tst')
assert pzl(tst) == (4361, 467835)

dat = read_str('03.dat')

print("day 3 puzzle =", pzl(dat))
