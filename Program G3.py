import numpy as np
import matplotlib.pyplot as plt




def P3():
    plt.close('all')
    coords = np.linspace(-3, 3, 21)
    x, v = np.meshgrid(coords, coords)
    w = 1 
    dxdt = v
    dvdt = - w **2 * x
    
    plt.figure(figsize=(6,6))
    plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('SHM')
    plt.quiver(x,v,dxdt,dvdt)
    plt.streamplot(x,v,dxdt,dvdt)
    
    
    plt.show()
    
P3()