from utils import read_str


def div(v, s, e):
    m = (e - s) // 2
    if v in ('F', 'L'):
        return s, s + m
    if v in ('B', 'R'):
        return s + m + 1, e
    raise ValueError


assert div('F', 0, 127) == (0, 63)
assert div('R', 0, 127) == (64, 127)
assert div('R', 64, 127) == (96, 127)
assert div('F', 96, 127) == (96, 111)


def search(p):
    s = 0
    e = 127
    for x in p[0:7]:
        s, e = div(x, s, e)
    r = s
    s = 0
    e = 7
    for x in p[7:]:
        s, e = div(x, s, e)
    c = s
    return r, c


def seat_id(p):
    r, c = search(p)
    return r * 8 + c


assert seat_id('BFFFBBFRRR') == 567


def pzl1(d):
    return max([seat_id(p) for p in d])


assert pzl1(['BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL']) == 820


def pzl2(d):
    t = [seat_id(p) for p in d]
    t.sort()
    for i, v in enumerate(t):
        if v + 1 != t[i + 1]:
            return v + 1


dat = read_str('05.dat')
print("day 5 puzzle 1 =", pzl1(dat))
print("day 5 puzzle 2 =", pzl2(dat))
