import numpy as np

mass = np.array([1, 2, 3])
count = 0


def mid_int(args):
    return sum(args) / len(args)


print(mid_int(mass))