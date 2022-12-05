from utils import read_re


def read(f: str) -> list:
    t = [list(map(int, s)) for s in read_re(f, r'(\d+)-(\d+),(\d+)-(\d+)')]
    return [(set(range(a1, b1+1)), set(range(a2, b2+1))) for a1, b1, a2, b2 in t]


def pzl1(ss) -> bool:
    return sum([a.issubset(b) or b.issubset(a) for a, b in ss])


def pzl2(ss):
    return sum([1 if a & b else 0 for a, b in ss])


dat = read("04.tst1")
assert pzl1(dat) == 2

dat = read("04.tst2")
assert pzl2(dat) == 4

dat = read("04.dat")

print("day 4 puzzle 1 =", pzl1(dat))
print("day 4 puzzle 2 =", pzl2(dat))

