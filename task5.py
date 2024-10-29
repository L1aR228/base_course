import numpy as np
N = int(input())
M = int(input())
trigonometry_array = np.zeros((N, M))
for i in range(N):
    for j in range(M):
        summ = np.sin(N * i + M * j + 1)
        if summ < 0:
            trigonometry_array[i, j] = 0

        else:
            trigonometry_array[i, j] = summ
# Скучный метод 
"""for line in trigonometry_array:
    for stolb in line:
        trigonometry_array[:, [1, 0]] = trigonometry_array[:, [1, 0]]
print(trigonometry_array)
"""
# ВРОДЕ НОРМ 
print(trigonometry_array[::-1])