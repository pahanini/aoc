from utils import read

import re


class Bag:

    def __init__(self):
        self.contains = {}

    def has(self, name):
        if name in self.contains:
            return True
        else:
            for _, b in self.contains.items():
                if b[1].has(name):
                    return True
        return False

    def cnt(self):
        c = 0
        for n, b in self.contains.items():
            c = c + b[0] + b[0]*b[1].cnt()
        return c


def parse(d):
    t = []
    d = d.replace("bags", "bag")
    r1 = re.compile(r'(([a-z ]+) contain (.+))\.')
    r2 = re.compile(r'(\d+) ([a-z ]+)')
    for _, n, c in r1.findall(d):
        t.append([n, [] if c == 'no other bag' else [r2.findall(x)[0] for x in c.split(',')]])
    return t


def create(d) -> dict:
    r = {}
    for v in d:
        r[v[0]] = Bag()
    for v in d:
        for c, n in v[1]:
            r[v[0]].contains[n] = (int(c), r[n])
    return r


def pzl1(bags, name):
    return sum([1 for _, b in bags.items() if b.has(name)])


def pzl2(bags, name):
    return bags[name].cnt()


tst1 = create(parse(read('07.1.tst')))
assert pzl1(tst1, 'shiny gold bag') == 4

tst2 = create(parse(read('07.2.tst')))
print(pzl2(tst2, 'dark blue bag'))
print(pzl2(tst2, 'dark violet bag'))

assert pzl2(tst2, 'shiny gold bag') == 126

dat = create(parse(read('07.dat')))

print("day 7 puzzle 1 =", pzl1(dat, 'shiny gold bag'))
print("day 7 puzzle 2 =", pzl2(dat, 'shiny gold bag'))
