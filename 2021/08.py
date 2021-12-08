from utils import read_str
from collections import defaultdict


def read(f):
    return [[list(filter(len, y.split(' '))) for y in x.split('|')] for x in read_str(f)]


def pzl1(p) -> int:
    r = 0
    for _, o in p:
        r += sum([1 for x in o if len(x) in (2, 3, 4, 7)])
    return r


# SCHEMA:
#
#  aa
# b  c
#  dd
# e  f
#  gg
def pzl2(dat):
    res = 0
    for patterns, out in dat:
        s = defaultdict(list)
        i = defaultdict(set)
        for pattern in patterns:
            s[len(pattern)].append(set(pattern))

        i[1] = s[2][0]
        i[8] = s[7][0]
        i[4] = s[4][0]
        i[7] = s[3][0]

        a = i[7] - i[1]
        dg = s[5][0] & s[5][1] & s[5][2] - a
        g = dg - i[4]
        d = dg - g
        bf = s[6][0] & s[6][1] & s[6][2] - a - g
        b = bf - i[1]
        f = bf - b
        c = i[1] - f
        e = i[8] - a - b - c - d - f - g

        t = [
            a | c | f | g | e | b,
            c | f,
            a | c | d | e | g,
            a | c | d | f | g,
            b | c | d | f,
            a | b | d | f | g,
            a | b | d | f | g | e,
            a | c | f,
            a | b | c | d | e | f | g,
            a | b | c | d | f | g,
        ]
        add = 0
        for i, k in enumerate(out):
            for j, l in enumerate(t):
                if set(k) == l:
                    add += 10 ** (3 - i) * j
        res += add
    return res


r = read('08.tst')

assert pzl1(r) == 26
assert pzl2(r) == 61229

r = read('08.dat')

print("day 8 puzzle 1 =", pzl1(r))
print("day 8 puzzle 2 =", pzl2(r))

