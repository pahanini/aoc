from utils import read_str


def pzl(chs) -> (int, int):
    p1 = 0
    p2 = []
    opn = "([{<"
    cls = ")]}>"
    score1 = (3, 57, 1197, 25137)
    for ch in chs:
        st = []
        for c in ch:
            if c in opn:
                st.append(c)
                continue
            p = st.pop()
            i = cls.index(c)
            if opn.index(p) != i:
                p1 += score1[i]
                break
        else:
            st.reverse()
            t = 0
            for p in st:
                t = t * 5 + opn.index(p) + 1
            p2.append(t)
    p2.sort()
    return p1, p2[len(p2)//2]


r = read_str('10.tst')
assert pzl(r) == (26397, 288957)

r = read_str('10.dat')
d1, d2 = pzl(r)

print("day 10 puzzle 1 =", d1)
print("day 10 puzzle 2 =", d2)
