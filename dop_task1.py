import matplotlib.pyplot as plt
import numpy as np


def lisaju(f):
    t = np.linspace(0, 100, 1000)
    fig, a = plt.subplots()
    a.clear()
    x = np.sin(0.1 * (f + 1) * t)
    y = np.sin(t)
    a.plot(x, y)
    plt.savefig('fig_12.png')


if __name__ == '__main__':
    lisaju(2)
