from utils import read_str

score = {
    'A': 1,  # Rock
    'B': 2,  # Paper
    'C': 3,  # Scissors
    'X': 1,
    'Y': 2,
    'Z': 3,
}


def pzl1(ss) -> int:
    r = 0
    for s in ss:
        a = score[s[0]]
        b = score[s[2]]
        t = b - a
        if t == 0:
            r += 3
        elif t == 1 or t == -2:
            r += 6
        r += b
    return r


def pzl2(ss) -> int:
    r = 0
    for s in ss:
        a = score[s[0]]
        t = score[s[2]]
        if t == 2:
            r += 3 + a
        elif t == 1:
            b = a - 1 if a > 1 else 3
            r += b
        else:
            b = a + 1 if a != 3 else 1
            r += 6 + b
    return r


tst = read_str('02.tst')

assert pzl1(tst) == 15
assert pzl2(tst) == 12

dat = read_str('02.dat')

print("day 2 puzzle 1 =", pzl1(dat))
print("day 2 puzzle 2 =", pzl2(dat))
