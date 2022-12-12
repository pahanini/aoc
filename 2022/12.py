import networkx as nx

from utils import read_str
from utils import op
from math import inf
from operator import add

dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

heights = {
    "S": 'a',
    "E": 'z',
}


def read(f: str):
    pp = {}          # points
    ee = {"A": []}   # ends
    for y, r in enumerate(read_str(f)):
        for x, c in enumerate(r):
            p = (x, y)
            if c in heights:
                ee[c] = p
                c = heights[c]
            pp[p] = ord(c)
            if c == 'a':
                ee["A"].append(p)

    g = nx.DiGraph()
    for p in pp:
        for d in dirs:
            np = op(add, p, d)
            if pp.get(np, inf) <= pp[p] + 1:
                g.add_edge(p, np)

    return g, ee


def pzl1(g, ee):
    return nx.shortest_path_length(g, ee["S"], ee["E"])


def pzl2(g, ee):
    p = []
    for s in ee["A"]:
        try:
            p.append(nx.shortest_path_length(g, s, ee["E"]))
        except nx.NetworkXNoPath:
            pass
    return min(p)


dat = read('12.tst')
assert pzl1(*dat) == 31
assert pzl2(*dat) == 29

dat = read('12.dat')

print("day 12 puzzle 1 =", pzl1(*dat))
print("day 12 puzzle 2 =", pzl2(*dat))
