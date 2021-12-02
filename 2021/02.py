from utils import read_re
import numpy as np

dirs = {
    "up": [0, -1],
    "down": [0, 1],
    "forward": [1, 0],
}


def pzl1(d) -> int:
    pos = np.array([0, 0])
    for d, c in d:
        pos += np.array(dirs[d]) * np.array([int(c), int(c)])
    return np.prod(pos)


def pzl2(d) -> int:
    pos = np.array([0, 0])
    aim = 0
    for d, c in d:
        c = int(c)
        aim += dirs[d][1] * c
        f = dirs[d][0] * c
        pos += np.array([f, aim * f])
    return np.prod(pos)


tst = read_re('02.tst', r"(.+) (.)")

assert pzl1(tst) == 150
assert pzl2(tst) == 900


dat = read_re('02.dat', r"(.+) (.)")

print("day 1 puzzle 1 =", pzl1(dat))
print("day 1 puzzle 2 =", pzl2(dat))
