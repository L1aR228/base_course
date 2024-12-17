import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
ax.set_aspect('equal')
circle = plt.Circle((0, 0), 0, color='b')
ax.add_artist(circle)


def update(frame):
    circle.set_radius(frame / 20)  # Увеличиваем радиус круга
    return circle,


ani = FuncAnimation(fig, update, frames=100, blit=True, interval=100, repeat=True)

ani.save('task_2.gif', writer="pillow")


'''import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
t = np.linspace(0, 12*np.pi, 1000)
def cirle_move(R, vx0, vy0, time):
    x = vx0 * time
    y = vy0 * time

    alpha = np.arange(0, 2*np.pi, 1)

    X = x * np.cos(t) - y * np.sin(t)
    Y = y * np.cos(t) + y * np.sin(t)

    return X, Y

fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='r', label='Ball')


def animate(i):
    ball.set_data(cirle_move(R=0.5, vx0=0.01, vy0=0.01, time=i))


edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames=100, interval=30)

plt.show()'''