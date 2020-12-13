from utils import read_str

import numpy as np


def parse(d):
    return int(d[0]), [(int(x) - i, int(x)) for i, x in enumerate(d[1].split(',')) if x != 'x']


# chinese remainder theorem
def crt(v):
    p = int(np.prod([x[1] for x in v]))
    t = 0
    for x, n in v:
        b = p // n
        t += x * b * pow(b, n - 2, n)
        t %= p
    return t


assert crt([(2, 3), (3, 5), (2, 7)]) == 23


def pzl1(d):
    t, bb = d
    mt, mb = 0, 0
    for _, b in bb:
        bt = b - t % b
        if mt > bt or mt == 0:
            mt, mb = bt, b
    return mt * mb


def pzl2(d):
    v = []
    for i, n in d[1]:
        v.append((i, n))
    return crt(v)


tst = parse(read_str('13.tst'))

assert pzl1(tst) == 295
assert pzl2(tst) == 1068781

dat = parse(read_str('13.dat'))

print("day 13 puzzle 1 =", pzl1(dat))
print("day 13 puzzle 2 =", pzl2(dat))
