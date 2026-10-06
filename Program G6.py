import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def G6Field():

    coords = np.linspace(-4, 4, 25)

    x, y = np.meshgrid(coords, coords)

    dxdt = y
    dydt = -x + (1 - x**2)*y

    plt.figure(figsize=(6,6))

    plt.quiver(x, y, dxdt, dydt, scale=750)
    plt.streamplot(x, y, dxdt, dydt)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Limit Cycle Vector Field')

    plt.show()

G6Field()

def P6(t, z):

    # Extract x and y from the state vector
    x = z[0]
    y = z[1]

    # Calculate the derivatives
    dxdt = y
    dydt = -x + (1 - x**2) * y

    # Return both derivatives
    return np.array([dxdt, dydt])

def P6main():
    
    t0 = 0
    tf = 30
    n = 1001
    t = np.linspace(t0, tf, n)
    initial_conditions = [
        (3, 3),       # (a)
        (-2, 2),      # (b)
        (0.1, 0.1),  # (c)
        (0.5, 1),     # (d)

        # Additional initial conditions
        (2, -2),
        (-3, -3),
        (1, 0)
    ]

    # Create grid of x and y values
    x_values = np.linspace(-4, 4, 25)
    y_values = np.linspace(-4, 4, 25)

    X, Y = np.meshgrid(x_values, y_values)

    # Calculate vector field
    U = Y
    V = -X + (1 - X**2) * Y

    # Calculate vector magnitude
    magnitude = np.sqrt(U**2 + V**2)

    # Normalise vectors so that the plot is easier to read
    U_norm = U / (magnitude + 1e-10)
    V_norm = V / (magnitude + 1e-10)

    plt.figure(figsize=(8, 7))

    plt.quiver(X, Y, U_norm, V_norm, magnitude,
               cmap='viridis')

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Vector Field")
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)


    plt.show()

    plt.figure(figsize=(8, 7))

    plt.streamplot(
        X, Y, U, V,
        density=1.5,
        color=magnitude,
        cmap='viridis'
    )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Streamlines")
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)
    plt.show()
    
P6main()