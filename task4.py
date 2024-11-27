import matplotlib.pyplot as plt
import numpy as np
k = 0.1
phi_max = 10 * np.pi 
e = 2.71828
def arhimed():

    p = np.arange(0, phi_max, 0.1)
    rho = k * p
    x1 = rho * np.cos(p)
    y1 = rho * np.sin(p)

    plt.plot(x1, y1)
    plt.axis('equal')

    plt.savefig('fig_8.png')
def log(b=0.2):
    p1 = np.linspace(0, phi_max, 1000)
    rho = np.exp(b * p1)
    x = rho * np.cos(p1)
    y = rho * np.sin(p1)

    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('fig_9.png')

def jezl():

    p = np.arange(-2* np.pi, phi_max, 0.1)
    rho = k / np.sqrt(p)
    x = rho * np.cos(p)
    y = rho * np.sin(p)

    plt.plot(x, y)
    plt.axis('equal')

    plt.savefig('fig_10.png')

def rose():
    k = 0.05
    p = np.arange(0, phi_max, 0.1)
    rho = np.sin(k * p)
    x = rho * np.cos(p)
    y = rho * np.sin(p)

    plt.plot(x, y)
    plt.axis('equal')

    plt.savefig('fig_11.png')
if __name__ =='__main__':
    jezl()