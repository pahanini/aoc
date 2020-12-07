from utils import read_groups


def pzl1(d):
    return sum([len(set(list("".join(g)))) for g in d])


def pzl2(d):
    return sum([len(set.intersection(*map(set, g))) for g in d])


tst = read_groups('06.tst')
assert pzl1(tst) == 11
assert pzl2(tst) == 6


dat = read_groups('06.dat')

print("day 6 puzzle 1 =", pzl1(dat))
print("day 6 puzzle 2 =", pzl2(dat))
