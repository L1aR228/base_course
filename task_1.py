
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

alpha = 0.1
num_frames = 100

fig, ax = plt.subplots()
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
circle, = ax.plot([], [], lw=2)

def init():
    circle.set_data([], [])
        return circle,
def update(frame):
     t = frame / 10
     r = alpha * t
     phi = np.linspace(0, 2 * np.pi, 100)
     x = r * np.cos(phi)
     y = r * np.sin(phi)
    circle.set_data(x, y)
        return circle,

ani = FuncAnimation(fig, update, frames=frames, interval=30)

ani.save('animation_5.gif', writer="pillow")

