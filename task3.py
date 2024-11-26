import matplotlib.pyplot as plt
import numpy as np
R = 100
def circle(a=100, b=50):

    x = np.linspace(-R, R, 100)
    y = np.linspace(-R, R, 100)

    x, y = np.meshgrid(x, y)

    fxy = (x**2 / a**2) + (y**2 / b**2)

    plt.contour(x, y, fxy, levels=[1])
    plt.axis('equal')

    plt.savefig('fig_7.png')

if __name__ =='__main__':
    circle()