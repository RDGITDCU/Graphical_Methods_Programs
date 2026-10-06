import numpy as np
import matplotlib.pyplot as plt

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
    plt.title('Verhulst Model')

    plt.show()
    
P4()
