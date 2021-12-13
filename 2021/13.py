import pytesseract
import numpy as np

from PIL import Image
from utils import read_groups


def read(f):
    gr = read_groups(f)
    return (
        {tuple(map(int, x.split(','))) for x in gr[0]},
        [(y[0][-1], int(y[1]))for y in [x.split('=') for x in gr[1]]]
    )


def fold(dots, instr):
    axis, val = instr
    new = set()
    for x, y in dots:
        if axis == 'y' and val < y:
            y = val - (y - val)
        if axis == 'x' and val < x:
            x = val - (x - val)
        new.add((x, y))
    return new


def pzl1(d):
    dots = fold(d[0], d[1][0])
    return len(dots)


def pzl2(d):
    dots = d[0]
    for inst in d[1]:
        dots = fold(dots, inst)
    mat = np.zeros((100, 100), dtype=np.uint8)  # experimental values
    for x, y in dots:
        mat[y+1][x+1] = 255
    img = Image.fromarray(mat)
    # img.save('13.png') uncomment if tesseract does not work
    img = img.resize((500, 500), Image.ANTIALIAS)  # experimental values
    return pytesseract.image_to_string(img)


dat = read('13.tst')
assert pzl1(dat) == 17

dat = read('13.dat')

print("day 13 puzzle 1 =", pzl1(dat))
print("day 13 puzzle 2 =", pzl2(dat))
