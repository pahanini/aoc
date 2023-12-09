from utils import read_groups
from itertools import cycle
from math import lcm
import re


def read(f) -> (dict, list):
    g = read_groups(f)
    return {a: (b, c) for a, b, c in [re.findall(r'\w+', v) for v in g[1]]}, g[0][0]


def pzl1(n, m, start='AAA', ends=lambda x: x == 'ZZZ'):
    i = {'L': 0, 'R': 1}
    c = start
    for s, d in enumerate(cycle(m), 1):
        c = n[c][i[d]]
        if ends(c):
            return s


def pzl2(n, m):
    ss = [k for k in n if k[-1] == 'A']
    return lcm(*[pzl1(n, m, start=s, ends=lambda x: x[-1] == 'Z') for s in ss])


n, m = read('08-1.tst')
assert pzl1(n, m) == 6
n, m = read('08-2.tst')
assert pzl2(n, m) == 6

n, m = read('08.dat')
print("day 8 puzzle part 1 =", pzl1(n, m))
print("day 8 puzzle part 2 =", pzl2(n, m))
