import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

R = 1
t = np.linspace(-13, 4 * np.pi, 100)  # эти значения подбирались 1000000000000 часов

x = R * (t - np.sin(t) ** 1)
y = R * (1 - np.cos(t) ** 1)

fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-15, 15)
ax.set_ylim(-15, 15)

ax.plot(x, y, label='Циклоида', color='blue')

line, = ax.plot([], [], 'o', color='r')

plt.grid()


def animate(i):
    line.set_data(x[i], y[i])
    return line,


ani = FuncAnimation(fig, animate, frames=100, interval=50)
plt.show() #Этот код нужно открывть строго в пайчарм 