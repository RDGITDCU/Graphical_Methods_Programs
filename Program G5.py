import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def LVfield():
    a = 4
    b = 2
    c = 1/3
    d = 1
    coords = np.linspace(-2, 10 , 21)
    x,y = np.meshgrid(coords,coords)
    dxdt = (a*x) - (b*x*y)
    dydt = (c*x*y) -(d*y)
    
    plt.figure(figsize=(6,6))
    plt.quiver(x, y, dxdt, dydt)
    plt.streamplot(x, y, dxdt, dydt)
    plt.xlabel('Rabbits, x')
    plt.ylabel('Foxes, y')
    plt.title(f'a = {a:.2f}, b = {b:.2f}, c = {c:.2f}, d = {d:.2f}')

    plt.show()
    
LVfield()