from utils import read_str
from collections import Counter, defaultdict
from itertools import combinations


def read(f):
    return [int(x) for x in read_str(f)[0].split(',')]


def pzl(p, two=False) -> int:
    c = Counter(p)
    f = defaultdict(int)
    for x, y in combinations(range(min(p), max(p) + 1), 2):
        if x not in c and y not in c:
            continue
        t = abs(x-y)
        if two:
            t = t * (t + 1) / 2
        f[x] += c[y] * t
        f[y] += c[x] * t
    return min(f.values())


d = read('07.tst')

assert pzl(d) == 37
assert pzl(d, True) == 168


d = read('07.dat')

print("day 7 puzzle 1 =", pzl(d))
print("day 7 puzzle 2 =", pzl(d, True))

