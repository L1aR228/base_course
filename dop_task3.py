import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

t = np.arange(0, 6 * np.pi, 0.1)


def circle_move(alpha):
    x = 12 * np.cos(t) + 8 * np.cos(1.5 * t)
    y = 12 * np.sin(t) - 8 * np.sin(1.5 * t)

    X = x * np.cos(alpha) - y * np.sin(alpha)
    Y = y * np.cos(alpha) + x * np.sin(alpha)

    return X, Y


fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='r', label='Ball')


def animate(i):
    alpha = i * np.radians(1)
    X, Y = circle_move(alpha)
    ball.set_data(X, Y)
    return ball,


edge = 30
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=1000, interval=10)
ani.save('dop_task_3.gif', writer="pillow")
