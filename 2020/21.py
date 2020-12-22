from utils import read_re
from collections import defaultdict


def parse(ss):
    food = []
    ings = set()
    ales = set()
    for ing, ale in ss:
        ing, ale = (set(ing.split(' ')), set(ale.split(', ')))
        ings.update(ing)
        ales.update(ale)
        food.append((ing, ale))
    return food, ings, ales


def pzl1(food, ings, ales):
    x = {i: ales.copy() for i in ings}
    c = defaultdict(int)
    for ii, aa in food:
        for a in aa:
            for i in ings:
                if i not in ii:
                    x[i].discard(a)
        for i in ii:
            c[i] += 1
    return sum([(c[i]) for i, a in x.items() if len(a) == 0]), x


def pzl2(x):
    u = set()
    e = len([i for i, a in x.items() if len(a) == 0])
    while len(u) + e < len(x):
        for i, a in x.items():
            if len(a) == 1:
                u.update(a)
            if len(a) > 1:
                x[i] = x[i] - u
    x = {i: a.pop() for i, a in x.items() if a}
    return ','.join([i for i, a in sorted(x.items(), key=lambda v: v[1])])


tst = parse(read_re('21.tst', r'([\w ]+) \(contains ([\w, ]+)\)'))
res = pzl1(*tst)

assert res[0] == 5
assert pzl2(res[1]) == 'mxmxvkd,sqjhc,fvjkl'

dat = parse(read_re('21.dat', r'([\w ]+) \(contains ([\w, ]+)\)'))
res = pzl1(*dat)

print("day 21 puzzle 1 =", res[0])
print("day 21 puzzle 2 =", pzl2(res[1]))
