from utils import read_str, op
from operator import add

dirs = [(0, 1), (-1, 1), (1, 1)]


def read(f: str) -> (set, int):
    r = set()
    b = 0
    for s in read_str(f):
        pp = [tuple(map(int, p.split(","))) for p in s.split(' -> ')]
        for (x0, y0), (x1, y1) in zip(pp, pp[1:]):
            for x in range(min(x0, x1), max(x0, x1) + 1):
                for y in range(min(y0, y1), max(y0, y1) + 1):
                    r.add((x, y))
                    b = max(b, y)
    return r, b


def pzl(r, b, p2=False):
    c = 0
    r = r.copy()
    sp = (500, 0)
    p = sp
    while True:
        p = sp
        while True:
            if not p2 and p[1] > b:
                return c
            for d in dirs:
                np = op(add, p, d)
                if np not in r and p[1] <= b:
                    p = np
                    break
            else:
                r.add(p)
                c += 1
                if p == sp:
                    return c
                break


dat = read('14.tst')

assert pzl(*dat) == 24
assert pzl(*dat, True) == 93

dat = read('14.dat')

print("day 14 puzzle 1 =", pzl(*dat))
print("day 14 puzzle 2 =", pzl(*dat, True))
