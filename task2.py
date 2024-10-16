import numpy as np 
import constant as co
v =  np.sqrt((10 * 100 * np.tan(35)**2) / 2 * (np.cos(45) ** 2) * (1 - np.tan(35) * np.tan(45)))
print(v)

n = 2 / (0.5 ** np.pi) * (co.h / (co.k * 200) ** (3/2)) * co.e ** (-300 / co.k * 200) * 300 ** (200 / 2)
print(n)