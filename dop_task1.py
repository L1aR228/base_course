import numpy as np

N1 = int(input())
M1 = int(input())
N2, M2 = int(input()), int(input())
trigonometry_array1 = np.zeros((N1, M1))
trigonometry_array2 = np.zeros(((N2, M2)))
for i in trigonometry_array1:
    for el in range(M1):
        n = int(input())
        i[el] = n
for i in trigonometry_array2:
    for el in range(M2):
        n = int(input())
        i[el] = n
print(trigonometry_array1)
print(trigonometry_array2)
print(np.maximum(trigonometry_array1, trigonometry_array2))
