from utils import read_groups
from collections import defaultdict


class Board:

    def __init__(self, numbers=[]):
        self.numbers = numbers
        self.occupied = []
        self.scores = defaultdict(int)

    def score(self, pos: tuple):
        for cid, v in enumerate(pos):
            key = (cid, v)
            self.scores[key] += 1
            if self.scores[key] == 5:
                return True
        return False

    def move(self, val) -> bool:
        try:
            i = self.numbers.index(val)
        except ValueError:
            return False
        pos = (i + 5) % 5, i // 5
        self.occupied.append(val)
        return self.score(pos)

    def unmarked(self) -> set:
        return set(self.numbers) - set(self.occupied)


t = Board()
assert not t.score((0, 0))
assert not t.score((1, 0))
assert not t.score((2, 0))
assert not t.score((3, 0))
assert t.score((4, 0))


def read(f):
    g = read_groups(f)
    n = [int(x) for x in g[0][0].split(",")]
    b = []
    for d in g[1:]:
        d = [int(d.strip()) for d in " ".join(d).split(" ") if d.strip() != ""]
        b.append(d)
    return n, b


def pzl1(nn, bb) -> int:
    bb = [Board(b) for b in bb]
    for n in nn:
        for b in bb:
            if b.move(n):
                return n * sum(b.unmarked())


def pzl2(nn, bb) -> int:
    won = []
    bb = [Board(b) for b in bb]
    for n in nn:
        for i, b in enumerate(bb):
            if i not in won:
                if b.move(n):
                    won.append(i)
                    if len(won) == len(bb):
                        return n * sum(b.unmarked())


nd, db = read('04.tst1')
assert pzl1(nd, db) == 4512
assert pzl2(nd, db) == 1924

nd, db = read('04.dat')
print("day 4 puzzle 1 =", pzl1(nd, db))
print("day 4 puzzle 2 =", pzl2(nd, db))

