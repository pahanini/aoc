from utils import read_groups
from re import findall
from collections import deque


def str_data(s: str) -> list:
    for i in range(0, len(s)//4 + 1):
        yield i, s[1 + i*4]


assert list(str_data('[Z] [M] [P]')) == [(0, 'Z'), (1, 'M'), (2, 'P')]
assert list(str_data('    [D]')) == [(0, ' '), (1, 'D')]


def data(f: str) -> (list, list):
    sch, mov = read_groups(f, False)
    sch.reverse()
    st = [deque() for _ in str_data(sch[0])]
    for r in sch[1:]:
        for k, v in str_data(r):
            if v != ' ':
                st[k].append(v)
    return st, [list(map(int, findall(r'\d+', m))) for m in mov]


def pzl(dat, part2) -> bool:
    st, mv = dat
    st = [t.copy() for t in st]
    for c, f, t in mv:
        h = []
        for i in range(0, c):
            h.append(st[f-1].pop())
        if part2:
            h.reverse()
        st[t-1] += h
    return ''.join([s.pop() for s in st])


def pzl2(ss):
    return sum([1 if a & b else 0 for a, b in ss])


d = data("05.tst")

assert pzl(d, False) == 'CMZ'
assert pzl(d, True) == 'MCD'

d = data("05.dat")

print("day 5 puzzle 1 =", pzl(d, False))
print("day 5 puzzle 2 =", pzl(d, True))
