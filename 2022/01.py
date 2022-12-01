from utils import read_groups


def pzl(gg, n) -> int:
    t = [sum([int(s) for s in g]) for g in gg]
    t.sort()
    return sum(t[-n:])


tst = read_groups('01.tst')

assert pzl(tst, 1) == 24000
assert pzl(tst, 3) == 45000

dat = read_groups('01.dat')

print("day 1 puzzle 1 =", pzl(dat, 1))
print("day 1 puzzle 2 =", pzl(dat, 3))
