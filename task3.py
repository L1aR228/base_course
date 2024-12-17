import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


t = np.linspace(0, 12 * np.pi, 1000) 
x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.sin(t / 12)**5)
y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) + np.sin(t / 12)**5)


fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)


# Начальная точка
line, = ax.plot([], [], color='b', lw=2)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    line.set_data(x[:frame], y[:frame])
    return line,

ani = FuncAnimation(fig, update, frames=100, interval=25)


ani.save('task_3.gif', writer="pillow")

