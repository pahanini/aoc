from utils import read_str
from z3 import Int, Solver, If
from re import findall


def read(f: str):
    return [list(map(int, findall(r"-?\d+", s))) for s in read_str(f)]


def m_dist(ax, ay, bx, by):
    return abs(ax - bx) + abs(ay - by)


def pzl1(d, y):
    b = set()
    o = set()
    for sx, sy, bx, by in d:
        b.add((bx, by))
        m = m_dist(sx, sy, bx, by)
        t = m - abs(sy - y)
        o |= set((x, y) for x in range(sx - t, sx + t + 1))
    return len(o - b)


def z3abs(x):
    return If(x >= 0, x, -x)


def pzl2(d, u):
    s = Solver()
    x = Int("x")
    y = Int("y")
    s.add(x >= 0)
    s.add(x <= u)
    s.add(y >= 0)
    s.add(y <= u)
    for sx, sy, bx, by in d:
        s.add(z3abs(x - sx) + z3abs(y - sy) > m_dist(sx, sy, bx, by))
    s.check()
    m = s.model()
    return m[x].as_long() * 4_000_000 + m[y].as_long()


dat = read('15.tst')

assert pzl1(dat, 10) == 26
assert pzl2(dat, 20) == 56_000_011

dat = read('15.dat')

print("day 15 puzzle 1 =", pzl1(dat, 2_000_000))
print("day 15 puzzle 2 =", pzl2(dat, 4_000_000))
