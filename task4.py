import numpy as np 
N = int(input())
M = int(input())
trigonometry_array = np.ones((N, M))
for i in trigonometry_array:
    for j in trigonometry_array:
        form = np.sin(N * i + M * j + 1)

for i in range(N):
    print(form)
