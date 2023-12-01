import networkx as nx

from utils import read_str
from re import findall


def read(f: str):
    g = nx.Graph()
    rates = {}
    for s in read_str(f):
        a, r, *t = findall(r'([A-Z]{2}|\d+)', s)
        rates[a] = int(r)
        for b in t:
            g.add_edge(a, b)
    print(g.nodes)
    t = nx.shortest_path_length(g, target='AA')


    print(t)

    exit()

    return g, rates


start = 'AA'


class State:

    


def pzl1(g: nx.Graph, rr: dict):
    good = set([k for k, v in rr.items() if v])
    visisted = []


    print(set(g.neighbors(start)) & good)
    #opnd = {}





dat = read('16.tst')
pzl1(*dat)

exit(0)

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
