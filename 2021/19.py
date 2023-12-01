from itertools import combinations, permutations, product
import numpy as np

def orientations():
    # 48
    rotations = []
    for permutation in permutations((0, 1, 2), 3):
        print(permutation)
        for signs in product((-1, 1), repeat=3):
            a = np.diag(signs)[:, permutation]
            #if np.linalg.det(a := np.diag(signs)[:, permutation]) > 0:
            print(a, np.linalg.det(a))
            rotations.append(a)

    return rotations



def gen_orientations():
    # 48
    for i in (-1, 1):
        for j in (-1, 1):
            for k in (-1, 1):
                for rest in permutations(range(3)):
                    yield rest + (i, j, k)


#print(len(orientations()))
#print(list(gen_orientations()))


def rotate(coord: tuple):
    for x, y, z in permutations(range(3)):
        for xf, yf, zf in product((-1, 1), repeat=3):
            t = coord[x]*xf, coord[y]*yf, coord[z]*zf
            yield t


rot = list(rotate((1, 2, 5)))
assert len(rot) == 48
print(rot)
print(len(set(rot)))
assert len(set(rot)) == 24

x => 1, y => 1, z => 1



