from utils import read_str
from collections import Counter


def ht(h, jokers):
    c = Counter(h)
    jc = c.pop("J", 0) if jokers else 0
    if jc == 5:
        return 7
    c = sorted(c.values())
    c[-1] += jc
    match c:
        case *_, 5:
            return 7
        case *_, 4:
            return 6
        case *_, 2, 3:
            return 5
        case *_, 3:
            return 4
        case *_, 2, 2:
            return 3
        case * _, 2:
            return 2
    return 1


def pzl(gg, jokers=False):
    hb = [g.split() for g in gg]  # hand & bid
    hb = sorted([
        (ht(h, jokers), *map("J23456789TJQKA".index, h), int(b))
        for h, b in hb
    ])
    return sum([
        i * b
        for i, (*_, b) in enumerate(hb, 1)
    ])


tst = read_str('07.tst')
assert pzl(tst) == 6440
assert pzl(tst, True) == 5905

dat = read_str('07.dat')
print("day 7 puzzle part 1 =", pzl(dat))
print("day 7 puzzle part 2 =", pzl(dat, True))
