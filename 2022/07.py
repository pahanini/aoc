from __future__ import annotations
from utils import read_str


class Dir:
    def __init__(self, parent=None, root=None):
        self.parent = parent
        self.root = self if root is None else root
        self.dirs = {}
        self.files = []

    def add(self, f: str):
        if f[0:3] == "dir":
            self.dirs[f[4:]] = Dir(self, self.root)
        else:
            self.files.append(f.split(" "))

    def cd(self, f: str) -> Dir:
        if f == "..":
            return self.parent
        elif f == "/":
            return self.root
        else:
            return self.dirs[f]

    def total(self) -> int:
        return sum([int(t[0]) for t in self.files]) + sum(
            [t.total() for t in self.dirs.values()]
        )

    def filter(self, val, fn):
        t = self.total()
        if fn(t):
            val.append(t)
        for d in self.dirs.values():
            d.filter(val, fn)


def read(f: str) -> Dir:
    cwd = Dir(None, None)
    for c in read_str(f):
        if c[0] == "$":
            if c[2:4] == "cd":
                cwd = cwd.cd(c[5:])
        else:
            cwd.add(c)
    return cwd.root


def pzl1(r: Dir) -> int:
    v = []
    r.filter(v, lambda a: a <= 100_000)
    return sum(v)


def pzl2(r: Dir) -> int:
    v = []
    req = 30_000_000 - (70_000_000 - r.total())
    r.filter(v, lambda t: t > req)
    return sorted(v)[0]


dat = read("07.tst")

assert pzl1(dat) == 95_437
assert pzl2(dat) == 24_933_642

dat = read("07.dat")

print("day 7 puzzle 1 =", pzl1(dat))
print("day 7 puzzle 2 =", pzl2(dat))
