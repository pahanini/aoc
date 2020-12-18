from utils import read_str
import re


class Op(int):
    def __mul__(self, b):
        return Op(int(self) + b)

    def __add__(self, b):
        return Op(int(self) + b)

    def __sub__(self, b):
        return Op(int(self) * b)


def pzl1(expr):
    expr = re.sub(r"(\d+)", r"Op(\1)", expr)
    expr = expr.replace("*", "-")
    return eval(expr, {}, dict(Op=Op))


def pzl2(expr):
    expr = re.sub(r"(\d+)", r"Op(\1)", expr)
    expr = expr.replace("*", "-")
    expr = expr.replace("+", "*")
    return eval(expr, {}, dict(Op=Op))


assert pzl1('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 13632
assert pzl2('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2') == 23340

dat = read_str('18.dat')


print("day 18 puzzle 1 =", sum([pzl1(s) for s in dat]))
print("day 18 puzzle 1 =", sum([pzl2(s) for s in dat]))