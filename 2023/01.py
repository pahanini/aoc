from utils import read_str

d = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']


def pzl(ss, replace=False) -> int:
    r = 0
    for s in ss:
        if replace:
            for k, v in enumerate(d):
                s = s.replace(v, v + str(k + 1) + v)
        t = [int(c) for c in s if c.isdigit()]
        r += 10 * t[0] + t[-1]
    return r


tst = read_str('01-1.tst')
assert pzl(tst) == 142

tst = read_str('01-2.tst')
assert pzl(tst, True) == 281

dat = read_str('01.dat')

print("day 1 puzzle 1 =", pzl(dat))
print("day 1 puzzle 2 =", pzl(dat, True))
