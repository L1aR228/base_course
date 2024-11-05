import numpy as np

mass = np.array([1, 2, 3])


def ymhojenie(args, count=1):
    for i in args:
        count *= i
    return count


print(ymhojenie(mass))