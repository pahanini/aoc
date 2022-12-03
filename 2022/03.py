from utils import read_str


def priority(c) -> int:
    v = ord(c) - 96
    return v if v > 0 else v + 58


def pzl1(ss) -> int:
    return sum([priority(list(set(s[:len(s)//2]) & set(s[len(s)//2:]))[0]) for s in ss])


def pzl2(ss) -> int:
    return sum([priority(list(set(ss[i]) & set(ss[i+1]) & set(ss[i+2]))[0]) for i in range(0, len(ss), 3)])


tst = read_str('03.tst')

assert pzl1(tst) == 157
assert pzl2(tst) == 70


dat = read_str('03.dat')

print("day 3 puzzle 1 =", pzl1(dat))
print("day 3 puzzle 2 =", pzl2(dat))
