
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
    reduction = 5
    q = plt.quiver(x[::reduction, ::reduction],y[::reduction, ::reduction],
                   vx[::reduction, ::reduction],vy[::reduction, ::reduction],
                   pivot='mid',
                   label = 'v_x = cos(x)*y , v_y = sin(x)*x'
                   )
    plt.legend()
    x_pos = 0.05
    y_pos = 0.985
    key_size = 2
    plt.quiverkey(q, x_pos, y_pos, key_size, 'Magnitude = 2', labelpos='E',coordinates='axes')
    plt.show()
    
#import run safety
if __name__ == '__main__':
    P1()

""" q = plt.quiver(x[::reduction, ::reduction], y[::reduction, ::reduction],  # coordinates at reduced density
                vx[::reduction, ::reduction], vy[::reduction, ::reduction],  # arrow x/y lengths at reduced density
                pivot='mid',  # position of the pivot of the arrow
                label='$v_x$ = cos($x$), $v_y$ = sin($y$)')  # label using LaTex notation
    """