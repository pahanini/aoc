from lark import Lark, LarkError
from utils import read_all
import re


def pzl1(d):
    rr, mm = d.split('\n\n')
    rr = re.sub(r'(\d+)', r'x\1', rr)
    lark = Lark(rr, start='x0')
    cnt = 0
    for m in mm.split():
        try:
            lark.parse(m)
        except LarkError:
            continue
        cnt += 1
    return cnt


def pzl2(d):
    return pzl1(d.replace('8: 42', '8: 42 | 42 8').replace('11: 42 31', '11: 42 31 | 42 11 31'))


tst = read_all('19.tst')
assert pzl1(tst) == 2

dat = read_all('19.dat')

print("day 19 puzzle 1 =", pzl1(dat))
print("day 19 puzzle 2 =", pzl2(dat))
