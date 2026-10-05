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
    
    plt.contourf(x, y, z, 20)  # plot a contour map using N=20 levels
    plt.contour(x,y,z, 20) 
    plt.set_cmap('coolwarm')
    
    red = 5
    xred, yred = x[::red, ::red], y[::red,::red]
    dxred, dyred = dx[::red, ::red], dy[::red,::red]
    
    plt.quiver(xred,yred,dxred,dyred,scale = 3)
    
    
    plt.show()
    
P2()
