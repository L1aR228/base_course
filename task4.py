import numpy as np 
N = int(input())
M = int(input())
trigonometry_array = np.zeros((N, M))
for i in range(N):
    for j in range(M):
        trigonometry_array[i, j] = np.sin(N * i)
        if trigonometry_array[i, j] < 0:
            trigonometry_array = 0
        else:
            pass
print(trigonometry_array)
