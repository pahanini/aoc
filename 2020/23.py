class Cup:
    _map = {}

    @classmethod
    def get(cls, n):
        return cls._map[n]

    @classmethod
    def create(cls, cups):
        cls._map = {}
        prev = first = Cup(cups.pop(0))
        for cup in cups:
            prev = Cup(cup, prev)
        prev.next = first
        return first

    def __init__(self, val, prev=None):
        Cup._map[val] = self
        self.val = val
        self.next = None
        if prev is not None:
            prev.next = self

    def pick(self):
        return [self.next, self.next.next, self.next.next.next]

    def dest(self, picked):
        last = len(Cup._map)
        res = self.val
        while True:
            res -= 1
            if res == 0:
                res = last
            if res not in [n.val for n in picked]:
                break
        return self.get(res)

    def move(self):
        picked = self.pick()
        dest = self.dest(picked)
        self.next = picked[2].next
        picked[2].next = dest.next
        dest.next = picked[0]
        return self.next


def solve(cups, n):
    cur = Cup.create(cups)
    for _ in range(0, n):
        cur = cur.move()


def pzl1(cups):
    cur = Cup.create(cups)
    for _ in range(0, 100):
        cur = cur.move()
    cur = Cup.get(1)
    res = []
    for _ in range(0, 8):
        cur = cur.next
        res.append(str(cur.val))
    return ''.join(res)


def pzl2(cups):
    cur = Cup.create(cups + list(range(10, 1_000_001)))
    for _ in range(0, 10_000_000):
        cur = cur.move()
    cur = Cup.get(1)
    return cur.next.val * cur.next.next.val


tst = list(map(int, '389125467'))
assert pzl1(tst.copy()) == '67384529'
assert pzl2(tst.copy()) == 149245887792

dat = list(map(int, '198753462'))
print("day 23 puzzle 1 =", pzl1(dat.copy()))
print("day 23 puzzle 2 =", pzl2(dat.copy()))
