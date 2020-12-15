from itertools import count
from collections import defaultdict


def pzl(n, y):
    s = defaultdict(list)
    for t in count(1):
        if t <= len(n):
            new = n[t-1]
        else:
            if len(s[lst]) == 1:
                new = 0
            else:
                new = s[lst][-1] - s[lst][-2]
        if t == y:
            return new
        s[new].append(t)
        lst = new


assert pzl([0, 3, 6], 2020) == 436

print("day 15 puzzle 1 =", pzl([19, 20, 14, 0, 9, 1], 2020))
print("day 15 puzzle 2 =", pzl([19, 20, 14, 0, 9, 1], 30000000))
