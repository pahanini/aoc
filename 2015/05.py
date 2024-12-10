from string import ascii_lowercase
from utils import read_str
from itertools import product

import re

vowels = "aeiou"
bad = ["ab", "cd", "pq", "xy"]


def pzl1(s):
    return (not any([r in s for r in bad]) and sum([s.count(r) for r in vowels]) >= 3
            and any([r + r in s for r in ascii_lowercase]))


def pzl2(s):
    pairs = [a + b for a, b in product(ascii_lowercase, ascii_lowercase)]
    triples = [a + b + a for a, b in product(ascii_lowercase, ascii_lowercase)]
    return any(s.count(p) > 1 for p in pairs) and any(t in s for t in triples)


assert pzl1("ugknbfddgicrmopn")
assert pzl1("aaa")
assert not pzl1("jchzalrnumimnmhp")
assert not pzl1("haegwjzuvuyypxyu")
assert not pzl1("dvszwmarrgswjxmb")

assert pzl2("qjhvhtzxzqqjkmpb")
assert pzl2("xxyxx")
assert not pzl2("uurcxstgmygtbstg")
assert not pzl2("ieodomkazucvgmuy")


ss = read_str('05.dat')

print("day 5 puzzle 1 =", sum([pzl1(s) for s in ss]))
print("day 5 puzzle 2 =", sum([pzl2(s) for s in ss]))

