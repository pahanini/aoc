from utils import read_groups
from collections import defaultdict

import numpy as np
import re


def is_val_matches_rule(r, v):
    return r[0] <= v <= r[1] or r[2] <= v <= r[3]


assert not is_val_matches_rule([1, 3, 5, 6], 4)
assert is_val_matches_rule([1, 3, 5, 6], 6)


def is_val_matches_any_rule(rr, v):
    return any([is_val_matches_rule(r, v) for _, r in rr.items()])


tr = {'a': [1, 3, 5, 6], 'b': [10, 20, 30, 40]}
assert not is_val_matches_any_rule(tr, 135)
assert is_val_matches_any_rule(tr, 35)


def is_list_matches_rule(r, vv):
    for v in vv:
        if not is_val_matches_rule(r, v):
            return False
    return True


assert is_list_matches_rule((1, 2, 4, 5), [1, 4])
assert not is_list_matches_rule((1, 2, 4, 5), [1, 6])

def get_ticket_error(rr, t):
    for v in t:
        if not is_val_matches_any_rule(rr, v):
            return v


assert get_ticket_error(tr, [135, 35]) == 135


def pzl1(d):
    rr, _, nn = d
    i = []
    for n in nn:
        e = get_ticket_error(rr, n)
        if e is not None:
            i.append(e)
    return sum(i)


def pzl2(d):
    rr, y, nn = d
    nn = np.array([n for n in nn if get_ticket_error(rr, n) is None])
    m = defaultdict(list)
    for rn, r in rr.items():
        for i in range(0, len(rr)):
            if is_list_matches_rule(r, nn[:, i]):
                m[rn].append(i)
    while True:
        o = [x[0] for _, x in m.items() if len(x) == 1]
        if len(o) == len(m):
            break
        for i, x in m.items():
            if len(x) > 1:
                m[i] = list(set(x) - set(o))
    r = [None] * len(rr)
    for i, x in m.items():
        r[x[0]] = i
    return np.prod([y[i] for i, m in enumerate(r) if m.startswith('departure')]), tuple(r)


def parse(g):
    r = {}
    for v in [re.search(r'([a-z ]+): (\d+)-(\d+) or (\d+)-(\d+)', v).groups() for v in g[0]]:
        r[v[0]] = list(map(int, v[1:]))
    y = [int(v) for v in g[1][1].split(',')]
    n = [list(map(int, v.split(',', ))) for v in g[2][1:]]
    return r, y, n


tst = parse(read_groups('16.1.tst'))
assert pzl1(tst) == 71

tst = parse(read_groups('16.2.tst'))
assert pzl2(tst) == (1, ('row', 'class', 'seat'))

dat = parse(read_groups('16.dat'))

print("day 16 puzzle 1 =", pzl1(dat))
print("day 16 puzzle 2 =", pzl2(dat)[0])
