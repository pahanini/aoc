from utils import read_groups, apply, op
from math import sqrt
from operator import sub, add

import numpy as np

top, rgt, btm, lft = 0, 1, 2, 3
opp = [2, 3, 0, 1]
deltas = {top: (0, -1), btm: (0, 1), lft: (-1, 0), rgt: (1, 0)}


def spinner(a):
    for _ in range(4):
        yield a
        yield np.flipud(a)
        a = np.rot90(a)


class Tile:

    def __init__(self, raw):
        self.id = int(raw[0].split(' ')[1][:-1])
        self.pxl = np.array([[c == '#' for c in s] for s in raw[1:]])
        self.rejected = []

    def get(self, edge):
        if edge == lft:
            s = self.pxl[:, 0]
        if edge == top:
            s = self.pxl[0]
        if edge == btm:
            s = self.pxl[-1]
        if edge == rgt:
            s = self.pxl[:, -1]
        return str(list(s))

    def match(self, tile):
        if tile in self.rejected:
            return None
        for spin in spinner(self.pxl):
            self.pxl = spin
            for edge in deltas.keys():
                if tile.get(edge) == self.get(opp[edge]):
                    return edge
        self.rejected.append(tile)


class Pic:

    def __init__(self, val):
        self.min = (0, 0)
        self.merged = None
        self.free = [Tile(s) for s in val]
        self.size = int(sqrt(len(self.free)))
        self.joined = {self.min: self.free.pop()}

    def join(self, tile, edge, pos):
        new = op(add, pos, deltas[edge])
        self.min = apply(min, self.min, new)
        self.joined[new] = tile
        self.free.remove(tile)

    def search(self):
        for pos, join in self.joined.items():
            for free in self.free:
                edge = free.match(join)
                if edge is not None:
                    self.join(free, edge, pos)
                    return

    def pzl1(self):
        while len(self.free) > 0:
            self.search()
        x0, y0 = self.min
        x1, y1 = x0 + self.size - 1, y0 + self.size - 1
        tiles = self.joined
        return tiles[(x0, y0)].id * tiles[(x1, y1)].id * tiles[(x0, y1)].id * tiles[(x1, y0)].id

    def pzl2(self, m):
        mask = np.array([[c == '#' for c in s] for s in m])
        merged = np.zeros((self.size*8, self.size*8), dtype=np.bool)
        for pos, joined in self.joined.items():
            x, y = op(sub, pos, self.min)
            merged[y*8:(y+1)*8, x*8:(x+1)*8] = joined.pxl[1:-1, 1:-1]

        def detect(t):
            s = 0
            for i in range(t.shape[0] - mask.shape[0]):
                for j in range(t.shape[1] - mask.shape[1]):
                    masked = t[i:i + mask.shape[0], j:j + mask.shape[1]]
                    if (masked >= mask).all():
                        s += 1
            return s

        return merged.sum() - max(map(detect, spinner(merged))) * mask.sum()


monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
]

tst = read_groups('20.tst')

pic = Pic(tst)
assert pic.pzl1() == 20899048083289
assert pic.pzl2(monster) == 273

dat = read_groups('20.dat')
pic = Pic(dat)

print("day 20 puzzle 1 =", pic.pzl1())
print("day 20 puzzle 2 =", pic.pzl2(monster))
