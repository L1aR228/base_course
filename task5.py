import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def fractal_points(x0, y0, C, D, n):
    x = np.zeros(n)
    y = np.zeros(n)
    x[0], y[0] = x0, y0

    for i in range(1, n):
        x[i] = x[i - 1] ** 2 - y[i - 1] ** 2 + C
        y[i] = 2 * x[i - 1] * y[i - 1] + D

    return x, y


x0 = 0.1
y0 = 0.1
C = 0.3
D = 0.33
point = 100  # количество точек

x, y = fractal_points(x0, y0, C, D, point)

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal')

point, = ax.plot([], [], '*', color='b')  # * выглядит круче всего

plt.grid()


def animate(i):
    point.set_data(x[:i], y[:i])  # Обновляем текущие точки
    return point,


ani = FuncAnimation(fig, animate, frames=100, interval=100)
ani.save('task_5.gif', writer="pillow")