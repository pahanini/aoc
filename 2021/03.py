from utils import read_str
import numpy as np
import operator


def read(f):
    return np.array([[int(c) for c in row] for row in read_str(f)])


def pzl1(d) -> int:
    e = ["0"] * d.shape[1]
    g = ["0"] * d.shape[1]
    for x in range(0, d.shape[1]):
        if np.bincount(d[:, x]).argmax() == 0:
            e[x] = "1"
        else:
            g[x] = "1"
    e = int("".join(e), 2)
    g = int("".join(g), 2)
    return g * e


def flt(d: np.array, op, pos=0):
    if len(d) <= 1:
        return int("".join([str(x) for x in d[0]]), 2)
    bc = np.bincount(d[:, pos])
    s = 1 if op(bc[1], bc[0]) else 0
    return flt(np.array([r for r in d if r[pos] == s]), op, pos + 1)


def pzl2(d) -> int:
    return flt(d, operator.ge) * flt(d, operator.lt)


tst = read('03.tst')

assert pzl1(tst) == 198
assert pzl2(tst) == 230


dat = read('03.dat')

print("day 3 puzzle 1 =", pzl1(dat))
print("day 3 puzzle 2 =", pzl2(dat))
