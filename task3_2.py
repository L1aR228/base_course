import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

t = np.linspace(0, 12 * np.pi, 1000)
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-30, 30)
ax.set_ylim(-30, 30)

# Начальная точка
line, = ax.plot([], [], color='r', lw=2)


def init():
    line.set_data([], [])
    return line,


def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,


ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True, interval=25)
ani.save('task_3_2.gif', writer="pillow")

