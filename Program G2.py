import numpy as np
import matplotlib.pyplot as plt



def P2():
    coords = np.linspace(-5,5,101)
    x, y = np.meshgrid(coords, coords)
    z = np.sqrt(x**2 + y**2)
    dx, dy = np.gradient(z)
    
    plt.figure(figsize=(6, 6))
    plt.gca().set_aspect('equal', adjustable='box')  
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.contourf(x, y, z, 25)  # plot a contour map using N=20 levels
    plt.contour(x,y,z,25, colors = 'k')
    plt.set_cmap('coolwarm')
    
    plt.show()
    
P2()
