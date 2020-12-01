from utils import read_int
from itertools import combinations

import numpy as np


def pzl(d, r):
    for x in combinations(d, r):
        if sum(x) == 2020:
            return np.prod(x)


tst = read_int('01.tst')

assert pzl(tst, 2) == 514579
assert pzl(tst, 3) == 241861950

dat = read_int('01.dat')

print("day 1 puzzle 1 =", pzl(dat, 2))
print("day 1 puzzle 2 =", pzl(dat, 3))
