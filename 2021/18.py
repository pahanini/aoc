from __future__ import annotations
from utils import read_str
from itertools import product


def read(f):
    return list(read_str(f))


class El:
    def __init__(self, val: int, parent: El = None):
        self.parent = parent
        self.left = None
        self.val = None
        self.right = None
        self.set(val)

    def set(self, val):
        if isinstance(val, int):
            self.left = None
            self.right = None
            self.val = val
        else:
            if isinstance(val[0], El):
                self.left = val[0]
                val[0].parent = self
            else:
                self.left = El(val[0], self)
            if isinstance(val[1], El):
                self.right = val[1]
                val[1].parent = self
            else:
                self.right = El(val[1], self)
            self.val = None

    def is_pair(self) -> bool:
        return self.val is None

    def mag(self) -> int:
        return self.left.mag() * 3 + self.right.mag() * 2 if self.is_pair() else self.val

    def list(self) -> list[El]:
        return self.left.list() + self.right.list() if self.is_pair() else [self]

    def lvl(self):
        if self.is_pair():
            return 1 if self.parent is None else 1 + self.parent.lvl()
        return self.parent.lvl()

    def __str__(self) -> str:
        return f"[{self.left},{self.right}]" if self.is_pair() else str(self.val)

    def is_explosive(self) -> bool:
        if self.is_pair():
            return self.lvl() > 4 and not self.left.is_pair() and not self.right.is_pair()
        else:
            return self.lvl() > 4 and self.parent.is_explosive()

    def is_splittable(self) -> bool:
        return not self.is_pair() and self.val > 9


def make(s: str) -> El:
    return El(eval(s))


el = make('[[9,1],[1,9]]')
assert el.mag() == 129
assert str(el) == '[[9,1],[1,9]]'

el = make('[1,[9,1]]')
assert el.mag() == 61
assert str(el) == "[1,[9,1]]"

lst = el.list()
assert len(lst) == 3
assert lst[0].lvl() == 1
assert lst[2].lvl() == 2


el = make('[[[[[9,8],1],2],3],4]')
lst = el.list()

assert lst[0].is_explosive()
assert lst[1].is_explosive()
assert not lst[2].is_explosive()


def explode(val: El):
    t = val.list()
    for i, v in enumerate(t):
        if v.is_explosive():
            if i > 0:
                t[i-1].val += v.val
            if i + 2 < len(t):
                t[i+2].val += t[i+1].val
            v.parent.set(0)
            return True
    return False


assert explode(el)
assert str(el) == '[[[[0,9],2],3],4]'

el = make('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]')
assert explode(el)
assert str(el) == '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'

el = make('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]')
assert explode(el)
assert str(el) == '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'


def split(val: El):
    t = val.list()
    for v in t:
        if v.is_splittable():
            v.set([v.val // 2, v.val - v.val // 2])
            return True
    return False


el = El(11)
assert split(el)
assert str(el) == '[5,6]'


def action(val: El):
    while explode(val):
        return True
    while split(val):
        return True
    return False


def reduce(val: El):
    while action(val):
        pass
    return val


el = make('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]')
reduce(el)
assert str(el) == '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'


def add(a: El, b: El) -> El:
    return reduce(El([a, b]))


a = make('[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]')
b = make('[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]')
assert str(add(a, b)) == '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]'


def mag(s: list[str]) -> int:
    f = add(make(s[0]), make(s[1]))
    if len(s) > 2:
        return mag([str(f)] + s[2:])
    return f.mag()


def max_mag(s: list[El]) -> int:
    return max([mag([s1, s2]) for s1, s2 in product(s, s) if s1 != s2])


dat = read('18.tst')
assert mag(dat) == 4140
assert max_mag(dat) == 3993


dat = read('18.dat')
print("day 18 puzzle 1 =", mag(dat))
print("day 18 puzzle 2 =", max_mag(dat))

