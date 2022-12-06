from utils import read_str


def pzl(s: str, x: int) -> int:
    for i in range(x-1, len(s)):
        if len(set(s[i-x+1:i+1])) == x:
            return i + 1


assert pzl("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
assert pzl("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11
assert pzl("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 14) == 19


d = read_str("06.dat")

print("day 6 puzzle 1 =", pzl(d[0], 4))
print("day 6 puzzle 2 =", pzl(d[0], 14))
