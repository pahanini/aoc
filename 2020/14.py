from utils import read_str
from itertools import product

import re


def mask1(m, v):
    mo = int(m.replace('X', '0'), 2)
    ma = int(m.replace('X', '1'), 2)
    return (v | mo) & ma


assert mask1('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X', 11) == 73


def extend(m):
    r = set()
    p = [i for i, c in enumerate(m) if c == 'X']
    f = product(["1", "0"], repeat=len(p))
    for x in product(["1", "0"], repeat=len(p)):
        for i, v in zip(p, x):
            m = m[:i] + v + m[i+1:]
        r.add(m)
    return r


assert extend("XX") == set(("10", "01", "11", "00"))


def mask2(m, v):
    r = set()
    v = bin(v)[2:].zfill(len(m))
    for i, t in enumerate(m):
        if t != '0':
            v = v[:i] + t + v[i + 1:]
    for e in extend(v):
        r.add(int(e, 2))
    return r


assert mask2('000000000000000000000000000000X1001X', 42) == {59, 26, 27, 58}
assert mask2('00000000000000000000000000000000X0XX', 26) == {16, 17, 18, 19, 24, 25, 26, 27}


def parse(d):
    d = [s.split(" = ") for s in d]
    return [(c, v) if c == 'mask' else (int(re.sub(r"\D", "", c)), int(v)) for c, v in d]


def pzl1(d):
    t = {}
    for c, v in d:
        if c == 'mask':
            m = v
        else:
            t[c] = mask1(m, v)
    return sum(t.values())


def pzl2(d):
    t = {}
    for c, v in d:
        if c == 'mask':
            m = v
        else:
            for a in mask2(m, c):
                t[a] = v
    return sum(t.values())


tst = parse(read_str('14.1.tst'))
assert pzl1(tst) == 165
tst = parse(read_str('14.2.tst'))
assert pzl2(tst) == 208

dat = parse(read_str('14.dat'))
print("day 14 puzzle 1 =", pzl1(dat))
print("day 14 puzzle 2 =", pzl2(dat))
