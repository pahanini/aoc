from utils import read_str
from operator import add, sub
from collections import defaultdict

moves = {
    'U': (0, -1),
    'R': (1, 0),
    'D': (0, 1),
    'L': (-1, 0),
}


def axis(h, t, same):
    if abs(h - t) == 2:
        return t + (h - t) // 2
    if abs(h - t) == 1 and same:
        return t + (h - t)
    return t


assert axis(1, 1, False) == 1
assert axis(1, 2, False) == 2
assert axis(1, 2, True) == 1


def pull(h, t):
    d = tuple(map(abs, map(sub, h, t)))
    same = sum([p > 1 for p in d]) > 0
    return tuple(map(axis, h, t, (same, same)))


assert pull((0, 0), (0, 0)) == (0, 0)
assert pull((0, 0), (1, 1)) == (1, 1)
assert pull((1, 2), (0, 0)) == (1, 1)


def pzl(ss, n=2) -> int:
    r = [(0, 0)] * n
    v = defaultdict(int)
    for s in ss:
        d, k = s.split(' ')
        for i in range(0, int(k)):
            r[0] = tuple(map(add, r[0], moves[s[0]]))
            for j in range(1, n):
                r[j] = pull(r[j-1], r[j])
            v[r[n-1]] += 1
    return len(v)


dat = read_str("09.tst")

assert pzl(dat, 2) == 13

dat = read_str("09.dat")

print("day 9 puzzle 1 =", pzl(dat, 2))
print("day 9 puzzle 2 =", pzl(dat, 10))
