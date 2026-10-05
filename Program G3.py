import numpy as np
import matplotlib.pyplot as plt




def P3():
    plt.close('all')
    coords = np.linspace(-3, 3, 21)
    x, y = np.meshgrid(coords, coords)
    