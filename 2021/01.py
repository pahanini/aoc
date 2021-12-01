from utils import read_int


def pzl(d, w) -> int:
    res = 0
    for i in range(1, len(d)):
        if sum((d[i:i+w])) > sum(d[i-1:i+w-1]):
            res += 1
    return res


tst = read_int('01.tst')

assert pzl(tst, 1) == 7
assert pzl(tst, 3) == 5

dat = read_int('01.dat')

print("day 1 puzzle 1 =", pzl(dat, 1))
print("day 1 puzzle 2 =", pzl(dat, 3))
