from utils import read_str
from collections import defaultdict


def read(f):
    r = defaultdict(list)
    for a, b in [ln.split('-') for ln in read_str(f)]:
        r[a].append(b)
        r[b].append(a)
    return r


def pzl1(g):
    paths = [['start']]
    found = 0
    while paths:
        path = paths.pop()
        last = path[-1]
        if last == 'end':
            found += 1
            continue
        neighbors = g[last]
        for neighbor in neighbors:
            if neighbor.islower() and neighbor in path:
                continue
            paths.append(path + [neighbor])
    return found


def pzl2(g):
    paths = [(['start'], False)]
    found = 0
    while paths:
        path, flag = paths.pop()
        last = path[-1]
        if last == 'end':
            found += 1
            continue
        neighbors = g[last]
        for neighbor in neighbors:
            new_flag = flag
            if neighbor.islower() and neighbor in path:
                if flag or neighbor == 'start':
                    continue
                else:
                    new_flag = True
            paths.append((path + [neighbor], new_flag))
    return found


dat = read('12.tst')
assert pzl1(dat) == 19

dat = read('12.dat')
print("day 12 puzzle 1 =", pzl1(dat))
print("day 12 puzzle 2 =", pzl2(dat))
