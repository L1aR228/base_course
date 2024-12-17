import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def chikl():
    R = 1  
    t = np.linspace(0, 8 * np.pi, 100)


    x = R * (t - np.sin(t) ** 3)  # лучшее значение 1
    y = R * (1 - np.cos(t) ** 3)


    plt.plot(x, y)
    plt.title("Циклоида")
    plt.axis('equal')
    plt.grid()
    plt.savefig('task_fig_1.png')

def aster():
    R = 1  
    t = np.linspace(0, 8 * np.pi, 100)


    x = R * (R * np.cos(t) ** 3)  # лучшее значение 1
    y = R * (R * np.sin(t) ** 3)


    plt.plot(x, y)
    plt.title("Циклоида")
    plt.axis('equal')
    plt.grid()
    plt.savefig('task_2.png')


if __name__ =='__main__':
    chikl()