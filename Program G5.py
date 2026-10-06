import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def LVfield():
    a = 4
    b = 2
    c = 1/3
    d = 1
    coords = np.linspace(0, 6 , 21)
    x,y = np.meshgrid(coords,coords)
    dxdt = (a*x) - (b*x*y)
    dydt = (c*x*y) -(d*y)
    seed = np.array([[4.0, 2.0]])
    
    plt.figure(figsize=(6,6))
    plt.quiver(x, y, dxdt, dydt,scale=500)
    plt.streamplot(x, y, dxdt, dydt,start_points=seed,color='red',linewidth=2)
    plt.xlabel('Rabbits, x')
    plt.ylabel('Foxes, y')
    plt.title(f'a = {a:.2f}, b = {b:.2f}, c = {c:.2f}, d = {d:.2f}')

    plt.show()
    
LVfield()

def LV(t, z):

    x = z[0]
    y = z[1]

    dxdt = a*x - b*x*y
    dydt = c*x*y - d*y

    return [dxdt, dydt]

def G5RK():

    global a, b, c, d

    a = 4.0
    b = 2.0
    c = 1/3
    d = 1.0
    t0 = -2
    tf = 10

    t = np.linspace(t0, tf, 500)

    x0 = 4.0
    y0 = 2.0

    result = integrate.solve_ivp(
        fun=LV,
        t_span=(t0, tf),
        y0=[x0, y0],
        method='RK45',
        t_eval=t
    )

    x = result.y[0]
    y = result.y[1]

    plt.figure(figsize=(6,6))

    plt.plot(result.t, x, label='Rabbits')
    plt.plot(result.t, y, label='Foxes')

    plt.xlabel('Time')
    plt.xlim(0,tf)
    plt.ylim(0)
    plt.ylabel('Population')

    plt.title(
        f'x0={x0}, y0={y0}'
    )

    plt.legend()

    plt.show()
    
    plt.figure(figsize=(6,6))

    plt.plot(x, y)
    plt.xlabel('Rabbits, x')
    plt.ylabel('Foxes, y')
    plt.title(f'x0={x0}, y0={y0}')
    plt.show()
    
G5RK()