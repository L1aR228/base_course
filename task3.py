import matplotlib.pyplot as plt
import numpy as np

def circle(x=10):

    x = np.arange(-2*R, 2*R, 0.1)
    y = np.arange(-2*R, 2*R, 0.1)

    x, y = np.meshgrid(x, y)

    fxy = x**2 + y**2 - R**2

    plt.contour(x, y, fxy, levels=[1])
    plt.axis('equal')

    plt.savefig('fig_7.png')

if __name__ =='__main__':
    circle()