from utils import read_str


def pzl(lines, two=False):
    count = 0
    for i, char in enumerate(lines[0]):
        count += 1 if char == '(' else -1
        if two and count == -1:
            return i + 1
    return count


d = read_str('01.dat')
assert pzl(['()())'], two=True) == 5

print("day 1 puzzle 1 =", pzl(d))
print("day 2 puzzle 2 =", pzl(d, two=True))

