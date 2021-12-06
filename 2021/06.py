from utils import read_str
from collections import deque


def read(f):
    return [int(x) for x in read_str(f)[0].split(',')]


def pzl(f, days) -> int:
    с = deque([0] * 9)
    for count in f:
        с[count] += 1
    for _ in range(days):
        с.rotate(-1)
        с[6] += с[8]
    return sum(с)


d = read('06.tst')

assert pzl(d, 18) == 26
assert pzl(d, 80) == 5934
assert pzl(d, 256) == 26984457539

d = read('06.dat')

print("day 6 puzzle 1 =", pzl(d, 80))
print("day 6 puzzle 2 =", pzl(d, 256))

