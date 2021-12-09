import numpy as np

from utils import read_str


def read(f):
    return [list(map(int, list(x))) for x in read_str(f)]


def neighbors(m, x, y):
    max_x = len(m[0]) - 1
    max_y = len(m) - 1
    if x > 0:
        yield x - 1, y
    if x < max_x:
        yield x + 1, y
    if y > 0:
        yield x, y - 1
    if y < max_y:
        yield x, y + 1


def lp(m) -> list:
    max_x = len(m[0]) - 1
    max_y = len(m) - 1
    res = []
    for x in range(0, max_x + 1):
        for y in range(0, max_y + 1):
            if all([m[y][x] < m[ny][nx] for nx, ny in neighbors(m, x, y)]):
                res.append((x, y))
    return res


def pzl1(m) -> int:
    res = 0
    for x, y in lp(m):
        res += m[y][x] + 1
    return res


def pzl2(m) -> int:
    u = []

    def basin(x, y) -> int:
        t = 0
        if m[y][x] != 9 and (x, y) not in u:
            t += 1
            u.append((x, y))
            for nx, ny in neighbors(m, x, y):
                t += basin(nx, ny)
        return t

    basins = []
    for px, py in lp(m):
        u = []
        basins.append(basin(px, py))

    basins.sort(reverse=True)
    return np.prod(basins[0:3])


r = read('09.tst')

assert pzl1(r) == 15
assert pzl2(r) == 1134

r = read('09.dat')

print("day 9 puzzle 1 =", pzl1(r))
print("day 9 puzzle 2 =", pzl2(r))
