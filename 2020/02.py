from utils import read_re


def pzl1(d):
    c = 0
    for x in d:
        if int(x[0]) <= x[3].count(x[2]) <= int(x[1]):
            c += 1
    return c


def pzl2(d):
    c = 0
    for x in d:
        p1 = int(x[0]) - 1
        p2 = int(x[1]) - 1
        ch = x[2]
        s = x[3]
        if (s[p1] == ch) ^ (s[p2] == ch):
            c += 1
    return c


ptn = r'(\d+)-(\d+) (\w+): (\w+)'
tst = read_re('02.tst', ptn)

assert pzl1(tst) == 2
assert pzl2(tst) == 1

dat = read_re('02.dat', ptn)

print("day 2 puzzle 1 =", pzl1(dat))
print("day 2 puzzle 2 =", pzl2(dat))
