from utils import read_groups
from collections import Counter, defaultdict


def read(f):
    gr = read_groups(f)
    return (
        gr[0][0],
        {(k[0:1], k[1:2]): v for k, v in [x.split(' -> ') for x in gr[1]]}
    )


def pzl(gr, steps):
    tpl, rules = gr
    old = Counter(zip(tpl, tpl[1:]))
    cnt = Counter(list(tpl))
    for _ in range(steps):
        new = defaultdict(int)
        for p in old:
            insert = rules[p]
            lft = (p[0], insert)
            rgt = (insert, p[1])
            cnt[insert] = cnt.get(insert, 0) + old.get(p)
            new[lft] += old[p]
            new[rgt] += old[p]
        old = new
    return max(cnt.values()) - min(cnt.values())


dat = read('14.tst')

assert pzl(dat, 10) == 1588
assert pzl(dat, 40) == 2188189693529


dat = read('14.dat')

print("day 14 puzzle 1 =", pzl(dat, 10))
print("day 14 puzzle 2 =", pzl(dat, 40))
