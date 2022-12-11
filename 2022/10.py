from utils import read_str
from PIL import Image

import numpy as np


def read(f: str):
    x = [1]
    for s in read_str(f):
        c = x[-1]
        x.append(c)
        if v := s[5:]:
            x.append(c + int(v))
    return x


def pzl1(x):
    return sum(i * x[i - 1] for i in (20, 60, 100, 140, 180, 220))


def pzl2(x):
    p = np.zeros((6, 40), dtype=np.uint8)
    for i, x in enumerate(x):
        r = i // 40
        if abs(i % 40 - x) <= 1:
            p[r, i - r * 40] = 255
    img = Image.fromarray(p)
    img.save('10.png')
    img.show()


dat = read("10.tst")

assert pzl1(dat) == 13140

dat = read("10.dat")

print("day 10 puzzle 1 =", pzl1(dat))
print("day 10 puzzle 2 =", pzl2(dat))
