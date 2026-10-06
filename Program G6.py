import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

"""
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
    plt.title('Vector Field')

    plt.show()

G6Field()
"""

def P6(t, z):

    x = z[0]
    y = z[1]
    dxdt = y
    dydt = -x + (1 - x**2) * y

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

        # Add
        (2, -2),
        (-3, -3),
        (1, 0)
    ]

    
    x_values = np.linspace(-4, 4, 25)
    y_values = np.linspace(-4, 4, 25)

    X, Y = np.meshgrid(x_values, y_values)


    U = Y
    V = -X + (1 - X**2) * Y

    magnitude = np.sqrt(U**2 + V**2)

    # Normalise
    U_norm = U / (magnitude + 1e-10)
    V_norm = V / (magnitude + 1e-10)

    plt.figure(figsize=(8, 7))
    plt.quiver(X, Y, U_norm, V_norm, magnitude,
               cmap='gnuplot')
    plt.streamplot(
        X, Y, U, V,
        density=1.5,
        color=magnitude,
        cmap='gnuplot'
    )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Vector Field")
    plt.xlim(-4, 4)
    plt.ylim(-4, 4)


    plt.show()
   


    plt.figure(figsize=(8, 6))

    for x0, y0 in initial_conditions:

        
        z0 = np.array([x0, y0])
        result = integrate.solve_ivp(
            fun=P6,
            t_span=(t0, tf),
            y0=z0,
            method="RK45",
            t_eval=t
        )
        plt.plot(
            result.t,
            result.y[0],
            label=f"x0={x0}, y0={y0}"
        )

    plt.xlabel("Time, t")
    plt.ylabel("x(t)")
    plt.title("x(t) for Different Initial Conditions")
    plt.xlim(0, tf)
    plt.legend()
    plt.show()


    # Plot y(t)
    plt.figure(figsize=(8, 6))

    for x0, y0 in initial_conditions:

        z0 = np.array([x0, y0])

        result = integrate.solve_ivp(
            fun=P6,
            t_span=(t0, tf),
            y0=z0,
            method="RK45",
            t_eval=t
        )

        # Plot y(t)
        plt.plot(
            result.t,
            result.y[1],
            label=f"x0={x0}, y0={y0}"
        )

    plt.xlabel("Time, t")
    plt.ylabel("y(t)")
    plt.title("y(t) for Different Initial Conditions")
    plt.xlim(0, tf)
    plt.legend()
    plt.show()


    # PHASE SPACE PLOT

    plt.figure(figsize=(8, 7))

    for x0, y0 in initial_conditions:

        z0 = np.array([x0, y0])

        result = integrate.solve_ivp(
            fun=P6,
            t_span=(t0, tf),
            y0=z0,
            method="RK45",
            t_eval=t
        )

        # Phase space: y versus x
        plt.plot(
            result.y[0],
            result.y[1],
            label=f"({x0}, {y0})"
        )

        plt.plot(
            x0,
            y0,
            'o',
            markersize=5
        )


    # ---------------------------------------------------------
    # Isoclines
    # ---------------------------------------------------------

    # x-isocline:
    # dx/dt = y = 0
    x_iso = np.linspace(-4, 4, 500)
    y_x_iso = np.zeros_like(x_iso)

    plt.plot(
        x_iso,
        y_x_iso,
        'k--',
        linewidth=2,
        label="x-isocline: y=0"
    )


    # y-isocline:
    # dy/dt = -x + (1-x^2)y = 0
    
    x1 = np.linspace(-4, -1.01, 500)
    x2 = np.linspace(-0.99, 0.99, 500)
    x3 = np.linspace(1.01, 4, 500)

    y1 = x1 / (1 - x1**2)
    y2 = x2 / (1 - x2**2)
    y3 = x3 / (1 - x3**2)

    plt.plot(
        x1, y1,
        'r--',
        linewidth=2,
        label="y-isocline: y=x/(1-x²)"
    )

    plt.plot(
        x2, y2,
        'r--',
        linewidth=2
    )

    plt.plot(
        x3, y3,
        'r--',
        linewidth=2
    )

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Phase Space")

    plt.xlim(-4, 4)
    plt.ylim(-4, 4)

    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.legend()
    plt.show()
    
P6main()