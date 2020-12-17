from utils import read_str
from itertools import product
from collections import Counter


def parse(d):
    st = set()
    for y, s in enumerate(d):
        for x, v in enumerate(s):
            if v == '#':
                st.add((x, y))
    return st


def pzl1(st, dim):
    st = set([v + (dim - 2) * (0,) for v in st])
    dd = [x for x in product((-1, 0, 1), repeat=dim) if x != dim * (0,)]
    for _ in range(6):
        cnt = Counter([tuple(map(sum, zip(c, d))) for c in st for d in dd])
        st = [k for k, v in cnt.items() if (k not in st and v == 3) or (k in st and v in (2, 3))]
    return len(st)


tst = parse(read_str('17.tst'))

assert pzl1(tst, 3) == 112
assert pzl1(tst, 4) == 848

dat = parse(read_str('17.dat'))

print("day 17 puzzle 1 =", pzl1(dat, 3))
print("day 17 puzzle 2 =", pzl1(dat, 4))
