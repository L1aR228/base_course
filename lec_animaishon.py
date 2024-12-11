import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib.animation import FuncAnimation 

fix, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw=2)

x, y = [], []

parametr = np.linspace(0, 2*np.pi, 100)

ax.set_xlim(0, 2*np.pi)
ax.set_ylim(-1,1)


def update(frame):
    x.append(frame)
    y.append(np.sin(frame))

    anim_object.set_data(x, y)

    return anim_object

ani = FuncAnimation(fix, update, parametr, interval=50)

ani.save('animation_1.gif', writer="pillow")
