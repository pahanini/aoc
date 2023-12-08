from utils import read_groups
from itertools import count


class Converter:

    def __init__(self):
        self.l = []
        self.u = []
        self.d = []

    def add(self, rr):
        l = []
        u = []
        d = []
        for r in rr:
            a, b, c = [int(t) for t in r.split()]
            l.append(b)
            u.append(b+c)
            d.append(a-b)
        self.l.append(l)
        self.u.append(u)
        self.d.append(d)

    def fwd(self, v):
        for ll, uu, dd in zip(self.l, self.u, self.d):
            for l, u, d in zip(ll, uu, dd):
                if l <= v <= u:
                    v += d
                    break
        return v

    def bwd(self, v):
        zz = list(zip(self.l, self.u, self.d))
        zz.reverse()
        for ll, uu, dd in zz:
            ll.reverse()
            uu.reverse()
            dd.reverse()
            for l, u, d in zip(ll, uu, dd):
                if l <= v - d <= u:
                    v -= d
                    break
        return v


def create(gg) -> (Converter, list):
    c = Converter()
    for g in gg[1:]:
        c.add(g[1:])
    return c, [int(d) for d in gg[0][0].split()[1:]]


def pzl1(gg):
    c, seeds = create(gg)
    ll = [c.fwd(s) for s in seeds]
    return min(ll)


def pzl2(gg):
    c, seeds = create(gg)
    for n in count():
        s = c.bwd(n)
        for l, r in zip(seeds[::2], seeds[1::2]):
            if l <= s < l + r:
                return n


c = Converter()
c.add(['50 98 2', '52 50 48'])
assert c.fwd(14) == 14
assert c.bwd(14) == 14
assert c.fwd(55) == 57
assert c.bwd(57) == 55
assert c.fwd(79) == 81
assert c.bwd(81) == 79

c = Converter()
c.add(['50 98 2', '52 50 48'])
c.add(['0 15 37', '37 52 2', '39 0 15'])
assert c.fwd(79) == 81
assert c.fwd(14) == 53


tst = read_groups('05.tst')
assert pzl1(tst) == 35
assert pzl2(tst) == 46

dat = read_groups('05.dat')
print("day 5 puzzle part 1 =", pzl1(dat))
print("day 5 puzzle part 2 =", pzl2(dat))
