from utils import read_str
from collections import Counter

import re

offsets = {'e': 2, 'se': 1-1j, 'sw': -1-1j, 'w': -2, 'nw': -1+1j, 'ne': 1+1j}


def pzl1(ss):
    bb = set()
    for s in ss:
        dd = re.findall('e|se|sw|w|nw|ne', s)
        x = {sum(offsets[d] for d in dd)}
        bb ^= x
    return len(bb), bb


def pzl2(ss):
    _, bb = pzl1(ss)
    for _ in range(100):
        count = Counter(b + o for o in offsets.values() for b in bb)
        bb = {w for w, n in count.items() if (w in bb and 1 <= n <= 2) or (w not in bb and n == 2)}

    return len(bb)


tst = read_str('24.tst')

assert pzl1(tst.copy())[0] == 10
assert pzl2(tst) == 2208

dat = read_str('24.dat')

print("day 24 puzzle 1 =", pzl1(dat)[0])
print("day 24 puzzle 2 =", pzl2(dat))
