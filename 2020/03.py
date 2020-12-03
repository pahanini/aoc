from utils import read_str


def pzl1(d, dx, dy):
    w = len(d[0])
    h = len(d)
    x = 0
    y = 0
    c = 0
    while True:
        x += dx
        y += dy
        if y > h - 1:
            return c
        if x > w - 1:
            x -= w
        if d[y][x] == '#':
            c += 1


def pzl2(d, d_list):
    res = 1
    for dx, dy in d_list:
        res *= pzl1(d, dx, dy)
    return res


tst = read_str('03.tst')

deltas = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

assert pzl1(tst, deltas[1][0], deltas[1][1]) == 7
assert pzl2(tst, deltas) == 336


dat = read_str('03.dat')

print("day 3 puzzle 1 =", pzl1(dat, deltas[1][0], deltas[1][1]))
print("day 3 puzzle 2 =", pzl2(dat, deltas))
