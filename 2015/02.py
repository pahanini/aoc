from utils import read_str
from math import prod

def pzl1(lines):
    res = 0
    for box in lines:
        l, w, h = map(int, box.split('x'))
        areas = [2 * l * w, 2 * w * h, 2 * h * l]
        slack = min(areas) // 2
        res += sum(areas) + slack

    return res


def pzl2(lines):
    res = 0
    for box in lines:
        dims = list(map(int, box.split('x')))
        res += (sum(dims) - max(dims))*2+prod(dims)
    return res


assert pzl1(['2x3x4']) == 58
assert pzl1(['1x1x10']) == 43
assert pzl2(['2x3x4']) == 34
assert pzl2(['1x1x10']) == 14

d = read_str('02.dat')

print("day 2 puzzle 1 =", pzl1(d))
print("day 2 puzzle 2 =", pzl2(d))

