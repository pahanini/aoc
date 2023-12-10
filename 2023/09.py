from utils import read_str
from itertools import count
import numpy as np


def read(f):
    return np.array([list(map(int, s.split())) for s in read_str(f)])


def pzl(n):
    s = 0
    for i in count():
        x = np.sum(np.diff(n, i)[:, -1])
        if x == 0:
            return s
        s += x


n = read('09.tst')
assert pzl(n) == 114

n = read('09.dat')

print("day 9 puzzle part 1 =", pzl(n))
print("day 9 puzzle part 2 =", pzl(np.flip(n, -1)))
