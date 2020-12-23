from utils import read_groups


def game(dd, mode):
    states = set()
    while min(map(len, dd)) > 0:
        state = tuple(map(tuple, dd))
        if state in states:
            return dd[0], 0
        states.add(state)
        cc = [d.pop(0) for d in dd]
        if all([c <= len(d) for c, d in zip(cc, dd)]) and mode == 2:
            _, w = game([d[:c] for d, c in zip(dd, cc)], mode)
        else:
            w = cc.index(max(cc))
        cc.insert(0, cc.pop(w))
        dd[w] += cc
    return dd[w], w


def pzl(gg, mode):
    d, _ = game([list(map(int, g[1:])) for g in gg], mode)
    return sum([(i + 1) * v for i, v in enumerate(reversed(d))])


tst = read_groups('22.tst')

assert pzl(tst, 1) == 306
assert pzl(tst, 2) == 291

dat = read_groups('22.dat')

print("day 22 puzzle 1 =", pzl(dat, 1))
print("day 22 puzzle 2 =", pzl(dat, 2))
