import numpy as np
import matplotlib.pyplot as plt




def P3():
    plt.close('all')
    coords = np.linspace(-3, 3, 21)
    x, v = np.meshgrid(coords, coords)
    w = 1 
    dxdt = v
    dvdt = - w **2 * x
    A = np.sqrt(dxdt **2 + dvdt**2)

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    # Left: full vector field
    ax[0].quiver(x, v, dxdt, dvdt)
    ax[0].streamplot(x, v, dxdt, dvdt)
    ax[0].set_title('Original')
    ax[0].set_xlabel('x')
    ax[0].set_ylabel('v')
    ax[0].set_aspect('equal')
    # Reduction, every 5th point
    red = 5

    ax[1].quiver(
    x[::red, ::red],
    v[::red, ::red],
    dxdt[::red, ::red],
    dvdt[::red, ::red]
    )
    ax[1].streamplot(x, v, dxdt, dvdt)
    ax[1].set_title('Reduced')
    ax[1].set_xlabel('x')
    ax[1].set_ylabel('v')
    ax[1].set_aspect('equal')

    plt.tight_layout()
    plt.show()


   
    
P3()

def P3SHMCon():
    plt.close('all')
    coords = np.linspace(-3, 3, 21)
    x, v = np.meshgrid(coords, coords)
    w = 1 
    dxdt = v
    dvdt = - w **2 * x
    a = np.sqrt(dxdt **2 + dvdt**2)
    
    plt.figure(figsize=(6,6))
    plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square
    plt.xlabel('x')
    plt.ylabel('v')
    plt.title('SHM')
    plt.quiver(x,v,dxdt,dvdt)
    lw = 3 * a/a.max()
    strm = plt.streamplot(x, v, dxdt, dvdt, linewidth=lw, color=a, cmap='gnuplot')
    plt.colorbar(strm.lines, fraction=0.046, pad=0.04)
    
    plt.show()
    
P3SHMCon()

  


def P3DHM():
    plt.close('all')
    coords = np.linspace(-3, 3, 21)
    x, v = np.meshgrid(coords, coords)
    w = 1 
    dxdt = v
    dvdt = - w **2 * x
    A = np.sqrt(dxdt **2 + dvdt**2)
    
    plt.figure(figsize=(6,6))
    plt.gca().set_aspect('equal', adjustable='box')  # Make plot box square
    plt.xlabel('x')
    plt.ylabel('v')
    plt.title('SHM')
    plt.quiver(x,v,dxdt,dvdt)
    plt.streamplot(x,v,dxdt,dvdt)

    