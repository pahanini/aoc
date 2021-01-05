def find(pub):
    s = 1
    while True:
        if pow(7, s, 20201227) == pub:
            return s
        s += 1


def pzl(pub1, pub2):
    return pow(pub2, find(pub1), 20201227)


assert pzl(5764801, 17807724) == 14897079

print(pzl(12090988, 240583))


