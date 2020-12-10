from utils import read_int
from itertools import combinations


def pzl1(n, l):

    def is_valid(x, y):
        for c in combinations(x, 2):
            if sum(c) == y:
                return True
        return False

    p = l
    while True:
        pre = n[p-l:p]
        if is_valid(pre, n[p]):
            p += 1
        else:
            return n[p]


def pzl2(n, x):
    for p in range(0, len(n) - 1):
        t = 2
        while sum(n[p:t]) < x:
            t += 1
        r = n[p:t]
        if sum(r) == x:
            return min(r) + max(r)


tst = read_int('09.tst')

assert pzl1(tst, 5) == 127
assert pzl2(tst, 127) == 62


dat = read_int('09.dat')

x = pzl1(dat, 25)
print("day 9 puzzle 1 =", x)
print("day 9 puzzle 2 =", pzl2(dat, x))
