from utils import read_str
from collections import defaultdict


def cnt(m, p, beam):
    r = 0
    x, y = p
    for dx, dy in ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)):
        if beam:
            c = '.'
            x0 = x
            y0 = y
            while c == '.':
                x0 += dx
                y0 += dy
                c = m[(x0, y0)]
        else:
            c = m[(x + dx, y + dy)]
        if c == '#':
            r += 1
    return r


def pzl(n, limit: int, beam: bool):
    while True:
        o = n.copy()
        t = 0
        for p, v in n.items():
            c = cnt(o, p, beam)
            if v == 'L' and c == 0:
                n[p] = '#'
                t += 1
            elif v == '#' and c >= limit:
                n[p] = 'L'
                t += 1
        if t == 0:
            return len([s for _, s in n.items() if s == '#'])


def parse(d):
    r = defaultdict(str)
    for y, s in enumerate(d):
        for x, c in enumerate(s):
            r[(x, y)] = c
    return r


tst = parse(read_str('11.1.tst'))
assert cnt(tst, (3, 4), False) == 2
assert cnt(tst, (3, 4), True) == 8

tst = parse(read_str('11.tst'))

assert pzl(tst.copy(), 4, False) == 37
assert pzl(tst.copy(), 5, True) == 26

dat = parse(read_str('11.dat'))

print("day 11 puzzle 1 =", pzl(dat.copy(), 4, False))
print("day 11 puzzle 2 =", pzl(dat.copy(), 5, True))
