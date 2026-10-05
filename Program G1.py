
import numpy as np
import matplotlib.pyplot as plt

def P1():
    x, y = np.meshgrid(np.linspace(0,2 * np.pi, 101), np.linspace(0,2 * np.pi,101))
    vx = np.cos(x) * y 
    vy = np.sin(x) * x
    plt.figure(figsize=(6, 6))
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Program 1')
    q = plt.quiver(x,y,vx,vy, pivot='mid',label = 'v_x = cos(x)*y , v_y = sin(x)*x')
    x_pos = 0.7
    y_pos = 0.98
    key_size = 2
    plt.quiverkey(q, x_pos, y_pos, key_size, 'Magnitude = 1', labelpos='E',coordinates='axes')
    plt.show()
    
#import run safety
if __name__ == '__main__':
    P1()
