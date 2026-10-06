import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
"""
def P4():

    r = 1
    K = 10

    x = np.linspace(-2, 15, 500)

    xdot = r * x * (1 - x/K)

    plt.figure(figsize=(6,6))

    plt.plot(x, xdot)

    plt.xlabel('x')
    plt.ylabel("x'")
    plt.xlim(-2, 15)
    plt.axhline(0,color='black')
    plt.title('')

    plt.show()
    
P4()

"""
def P4():

    r = 1
    K = 10

    x = np.linspace(-2, 15, 500)

    xdot = r * x * (1 - x/K)

    plt.figure(figsize=(6,6))

    plt.plot(x, xdot)

    plt.xlabel('x')
    plt.ylabel("x'")
    plt.xlim(-2, 15)

    plt.axhline(0, color='black')

    # Flow-on-a-line overlay
    xflow = np.linspace(-2, 15, 20)
    yflow = np.zeros_like(xflow)

    xdotflow = r * xflow * (1 - xflow/K)

    direction = np.sign(xdotflow)
    
    for i in range(len(xflow)):
        if direction[i] > 0:
            plt.quiver(
                       xflow[i],
                       yflow[i],
                       direction[i],
                       0,
                       color='green',
                       scale=25
                       )
        elif direction[i] < 0:
            plt.quiver(
                xflow[i],
                yflow[i],
                direction[i],
                0,
                color='red',
                scale=25
                )
        
  


    
   
    plt.axvline(0, linestyle='--', color='grey')
    plt.axvline(K, linestyle='--', color='grey')

    plt.title(f'k={K} , r = {r}')

    plt.show()

P4()

def verhulst(t, x):
    return r * x * (1 - x/K)

def P4B():

    global r, K

    r = 0.5
    K = 8
    t0 = 0
    tf = 20
    n = 201
    t = np.linspace(t0, tf, n)
    initial_conditions = [0.1, 1, 5, 15]
    plt.figure(figsize=(6,6))

    for x0 in initial_conditions:

        result = integrate.solve_ivp(
            fun=verhulst,
            t_span=(t0, tf),
            y0=[x0],
            method='RK45',
            t_eval=t
        )

        plt.plot(
            result.t,
            result.y[0],
            label=f'x0={x0}'
        )

    plt.xlabel('Time (s)')
    plt.xlim(0,tf)
    plt.ylim(0)
    plt.ylabel('Population, x(t)')
    plt.title(f'r={r}, K={K}')
    plt.legend()
    plt.show()
    
P4B()