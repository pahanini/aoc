from utils import read_str


def read(f):
    global C, R
    t = read_str(f)
    R = len(t)
    C = len(t[0])
    r = {}
    for x in range(0, C):
        for y in range(0, R):
            r[(x, y)] = int(t[y][x])
    return r


C = 0
R = 0


def neighbors(p):
    x, y = p
    for nx, ny in ((x+1, y), (x-1, y), (x, y+1), (x, y-1), (x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)):
        if 0 <= nx < C and 0 <= ny < R:
            yield nx, ny


def step(oo) -> (dict, int):
    for p in oo:
        oo[p] += 1
    flashed = set()
    while True:
        flashing = {p for p, o in oo.items() if o > 9} - flashed
        if not flashing:
            for p in flashed:
                oo[p] = 0
            return len(flashed)
        flashed |= flashing
        for p in flashing:
            for np in neighbors(p):
                oo[np] += 1


def pzl1(val):
    oo = dict(val)
    return sum([step(oo) for _ in range(0, 100)])


def pzl2(val):
    oo = dict(val)
    total = C * R
    i = 1
    while total != step(oo):
        i += 1
    return i


dat = read('11.tst')
assert pzl1(dat) == 1656
assert pzl2(dat) == 195


dat = read('11.dat')
print("day 11 puzzle 1 =", pzl1(dat))
print("day 11 puzzle 2 =", pzl2(dat))
