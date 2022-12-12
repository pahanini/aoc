from utils import read_all as read_all
import math


def read(f):
    res = list(map(int, bin(int(read_all(f), 16))[2:]))
    if len(res) % 4 != 0:
        res = ([0] * (4 - len(res) % 4)) + res
    return res


def to_int(bits):
    r = []
    for b in bits:
        r.append(str(b))
    return int(''.join(r), 2)


total_ver = 0

op = {
    0: sum,
    1: math.prod,
    2: min,
    3: max,
    5: lambda l: int(l[0] > l[1]),
    6: lambda l: int(l[0] < l[1]),
    7: lambda l: int(l[0] == l[1]),
}


def decode(packet, idx=0):
    global total_ver
    version = to_int(packet[idx:idx + 3])
    total_ver += version
    typ = to_int(packet[idx + 3:idx + 6])
    idx += 6
    if typ == 4:
        r = []
        while True:
            group = packet[idx:idx + 5]
            idx += 5
            r += group[1:]
            if group[0] == 0:
                break
        return idx, to_int(r)
    else:
        length_typ = packet[idx]
        idx += 1
        r = []
        if length_typ == 0:
            total_length = to_int(packet[idx:idx + 15])
            idx += 15
            orig_idx = idx
            while True:
                idx, rest = decode(packet, idx)
                r.append(rest)
                if idx - orig_idx == total_length:
                    break
                assert idx - orig_idx < total_length
        else:
            count_packets = to_int(packet[idx:idx + 11])
            idx += 11
            for i in range(count_packets):
                idx, rest = decode(packet, idx)
                r.append(rest)
        return idx, op[typ](r)


def pzl1(b):
    global total_ver
    total_ver = 0
    decode(b)
    return total_ver


def pzl2(b):
    _, r = decode(b)
    return r


dat = read('16.1.tst')
assert pzl1(dat) == 31
dat = read('16.2.tst')
assert pzl2(dat) == 9

dat = read('16.dat')

print("day 16 puzzle 1 =", pzl1(dat))
print("day 16 puzzle 2 =", pzl2(dat))
