from utils import read_str

dirs = {'N': 1j, 'E': 1, 'S': -1j, 'W': -1}
rot = {'L': 1j, 'R': -1j}


def pzl1(x):
    p = 0
    d = 1
    for c, v in x:
        if c in dirs:
            p += dirs[c] * v
        elif c in rot:
            d *= rot[c] ** (v / 90)
        else:
            p += d * v
    return abs(p.real) + abs(p.imag)


def pzl2(x):
    p = 0
    w = 10 + 1j
    for c, v in x:
        if c in dirs:
            w += dirs[c] * v
        elif c in rot:
            w *= rot[c] ** (v / 90)
        else:
            p += w * v
    return abs(p.real) + abs(p.imag)


def parse(d):
    return [(s[0], int(s[1:])) for s in d]


tst = parse(read_str('12.tst'))
assert pzl1(tst) == 25
assert pzl2(tst) == 286

dat = parse(read_str('12.dat'))

print("day 12 puzzle 1 =", pzl1(dat))
print("day 12 puzzle 2 =", pzl2(dat))
