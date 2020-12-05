from utils import read_str

import re


def is_year(s, f, t):
    return re.search(r'^\d{4}$', s) is not None and f <= int(s) <= t


assert is_year('1920', 1920, 1920)
assert not is_year('1920a', 1920, 1920)
assert not is_year('1920', 1921, 1922)


def is_height(s):
    t = re.search(r'^(\d+)(cm|in)$', s)
    if t is None:
        return False
    h, m = t.groups()
    return 150 <= int(h) <= 193 if m == 'cm' else 59 <= int(h) <= 76


assert not is_height('182mm')
assert not is_height('200cm')
assert not is_height('77in')
assert is_height('76in')
assert is_height('160cm')


def is_hair_color(s):
    return re.search(r'^#[a-f0-9]{6}$', s) is not None


assert is_hair_color('#ee12aa')
assert not is_hair_color('ee12aa')
assert not is_hair_color('#a213za')
assert not is_hair_color('#a122')


def is_eye_color(s):
    return s in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')


assert is_eye_color('amb')
assert not is_eye_color('xx')


def is_passport_id(s):
    return re.search(r'^\d{9}$', s) is not None


assert is_passport_id('000000000')
assert not is_passport_id('00000000A')
assert not is_passport_id('0000000001')


def pzl(d, validate=False):
    c = 0
    f = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
    for p in d:
        if 'cid' not in p:
            p['cid'] = None
        diff = list(set(f) - set(p.keys()))
        if len(diff) != 0:
            continue
        if not validate or (is_year(p['byr'], 1920, 2002) and is_year(p['iyr'], 2010, 2020)
                            and is_year(p['eyr'], 2020, 2030) and is_height(p['hgt'])) and is_hair_color(p['hcl']) \
                            and is_eye_color(p['ecl']) and is_passport_id(p['pid']):
            c += 1
    return c


def parse(d) -> []:
    ptn = r'([a-z]{3}):([a-z0-9#]+)'
    r = []
    p = {}
    for s in d:
        t = re.findall(ptn, s)
        if len(t) == 0:
            r.append(p)
            p = {}
        else:
            for k, v in t:
                p[k] = v
    r.append(p)
    return r


tst = parse(read_str('04.1.tst'))
assert pzl(tst) == 2

tst = parse(read_str('04.2.tst'))
assert pzl(tst, validate=True) == 0

tst = parse(read_str('04.3.tst'))
assert pzl(tst, validate=True) == 4


dat = parse(read_str('04.dat'))

print("day 4 puzzle 1 =", pzl(dat))
print("day 4 puzzle 2 =", pzl(dat, validate=True))
