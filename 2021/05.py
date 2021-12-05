from utils import read_re
from collections import defaultdict


def read(f):
    return [tuple(map(int, x)) for x in read_re(f, r"(\d+),(\d+) -> (\d+),(\d+)")]


def cmp(a, b):
    return (b > a) - (b < a)


def pzl(c, dia=False) -> int:
    f = defaultdict(int)
    for x0, y0, x1, y1 in c:
        dx = cmp(x0, x1)
        dy = cmp(y0, y1)
        if not dia and dx and dy:
            continue
        while (x0, y0) != (x1 + dx, y1 + dy):
            f[(x0, y0)] += 1
            x0 += dx
            y0 += dy
    return sum([1 for p in f.values() if p > 1])


d = read('05.tst')

assert pzl(d) == 5
assert pzl(d, True) == 12

d = read('05.dat')

print("day 5 puzzle 1 =", pzl(d))
print("day 5 puzzle 2 =", pzl(d, True))

