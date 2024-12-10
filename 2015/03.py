from utils import read_str
from itertools import cycle

moves = {
    '^': 1j,
    '>': 1,
    'v': -1j,
    '<': -1,
}


def pzl(lines, santa_count=1):
    start_pos = 0 + 0j
    pos = [start_pos] * santa_count
    indexes = cycle(range(santa_count))
    houses = {start_pos}
    for move in lines[0]:
        index = next(indexes)
        pos[index] += moves[move]
        houses.add(pos[index])
    return len(houses)


assert pzl(['>']) == 2
assert pzl(['^>v<']) == 4
assert pzl(['^v^v^v^v^v']) == 2
assert pzl(['^v'], 2) == 3
assert pzl(['^>v<'], 2) == 3
assert pzl(['^v^v^v^v^v'], 2) == 11

d = read_str('03.dat')

print("day 3 puzzle 1 =", pzl(d))
print("day 2 puzzle 2 =", pzl(d, 2))

