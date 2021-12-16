from utils import read_str

import networkx as nx
import numpy as np


def read(f):
    ln = read_str(f)
    return np.array([list(map(int, list(v))) for v in ln])


def pzl(val, x5=False):
    if x5:
        val = np.block([[val + x + y for x in range(5)] for y in range(5)])
        val[val > 9] -= 9

    g = nx.grid_2d_graph(*val.shape, create_using=nx.DiGraph)
    for _, v, d in g.edges(data=True):
        d["weight"] = val[v]
    source, *_, target = g.nodes
    return nx.shortest_path_length(g, source, target, weight="weight")


dat = read('15.tst')

assert pzl(dat) == 40
assert pzl(dat, True) == 315

dat = read('15.dat')

print("day 15 puzzle 1 =", pzl(dat))
print("day 15 puzzle 2 =", pzl(dat, True))
