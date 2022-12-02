from utils import read_str

lft = 'ABC'
rgt = 'XYZ'
loose = [1, 2, 0]


def pzl1(ss) -> int:
    r = 0
    for s in ss:
        elf = lft.index(s[0])
        me = rgt.index(s[2])
        if elf == me:
            r += 3
        elif loose[me] != elf:
            r += 6
        r += me + 1
    return r


def pzl2(ss) -> int:
    r = 0
    for s in ss:
        elf = lft.index(s[0])
        me = rgt.index(s[2])
        if me == 1:
            r += 3
            me = elf
        elif me == 2:
            r += 6
            me = loose[elf]
        else:
            me = loose.index(elf)
        r += me + 1
    return r


tst = read_str('02.tst')

assert pzl1(tst) == 15
assert pzl2(tst) == 12

dat = read_str('02.dat')

print("day 2 puzzle 1 =", pzl1(dat))
print("day 2 puzzle 2 =", pzl2(dat))
