from utils import read_int
from collections import defaultdict


def pzl1(n):
    diffs = []
    n.sort()
    p = 0
    for t in n:
        diffs.append(t-p)
        p = t
    return diffs.count(1) * (diffs.count(3) + 1)


def pzl2(n):
    pc = defaultdict(int)
    pc[0] = 1
    n.insert(0, 0)
    n.sort()
    for i, t in enumerate(n):
        pre = [x for x in n[max(i-3, 0):i] if t - x <= 3]
        if i > 0:
            s = 0
            for j in pre:
                s += pc[j]
            pc[t] = s
    return s


tst = read_int('10.tst')

assert pzl1(tst) == 220
assert pzl2(tst) == 19208

dat = read_int('10.dat')

print("day 10 puzzle 1 =", pzl1(dat))
print("day 10 puzzle 2 =", pzl2(dat))
