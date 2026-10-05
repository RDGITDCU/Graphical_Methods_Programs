
import numpy as np
import matplotlib.pyplot as plt

def P1():
    x, y = np.meshgrid(np.linspace(0,np.pi, 101), np.linspace(0,np.pi,101))
    vx = np.cos(x) * y 
    vy = np.sin(x) * x
    plt.figure(figsize=(8, 8))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Program 1')
    plt.quiver(x,y,vx,vy, pivot='mid',label = 'v_x = cos(x)*y , v_y = sin(x)*x')
    plt.legend()
    plt.show()
    
#import run safety
if __name__ == '__main__':
    P1()

