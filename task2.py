import matplotlib.pyplot as plt
import numpy as np

	
	
def parabola_plotter(k=1):
 
    x = np.linspace(-100,100,100)
    y = k/x
 
    plt.plot(x, y)

 
    plt.savefig('fig_6.png')
 
 
if __name__ == '__main__':
    parabola_plotter()