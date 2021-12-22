from utils import read_re


def read(f):
    t = read_re(f, r'x=(\d+)..(\d+), y=(-\d+)..(-\d+)')[0]
    return list(map(int, t))


def ok(x1, x2, y1, y2, xv, yv):
    x = 0
    y = 0
    while not (x > x2 or y < y1 or (xv == 0 and not x1 <= x <= x2)):
        x += xv
        y += yv
        if x1 <= x <= x2 and y1 <= y <= y2:
            return True
        xv = max(0, xv - 1)
        yv -= 1
    return False


def hits(x1, x2, y1, y2):
    xv_max = x2
    xv_min = 1
    yv_min = y1
    yv_max = 1 - y1
    for xv in range(xv_min, xv_max + 1):
        for yv in range(yv_min, yv_max):
            if ok(x1, x2, y1, y2, xv, yv):
                yield xv, yv


def pzl1(d):
    return max([v * (v + 1) // 2 for _, v in hits(*d)])


def pzl2(d):
    return len(list(hits(*d)))


dat = read('17.tst')
assert ok(*dat, 7, 2)
assert ok(*dat, 6, 3)
assert ok(*dat, 9, 0)
assert not ok(*dat, 17, -4)

assert pzl1(dat) == 45
assert pzl2(dat) == 112

dat = read('17.dat')

print("day 17 puzzle 1 =", pzl1(dat))
print("day 17 puzzle 2 =", pzl2(dat))
