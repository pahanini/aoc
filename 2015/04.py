from hashlib import md5


def pzl(key, prefix):
    i = 0
    while True:
        v = md5((key + str(i)).encode('utf-8')).hexdigest()
        if v.startswith(prefix):
            return i
        i += 1


print("day 4 puzzle 1 =", pzl("bgvyzdsv", "00000"))
print("day 4 puzzle 2 =", pzl("bgvyzdsv", "000000"))

