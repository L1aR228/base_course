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

a = N - 1
b = M - 1

trigonometry_array[:, a], trigonometry_array[:][b] = trigonometry_array[:, b], trigonometry_array[:][a]

print(trigonometry_array)


