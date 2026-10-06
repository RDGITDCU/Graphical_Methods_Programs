import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def P6():
    tmax = 30
    dxdt = y
    dydt = -x +(1 - x**2) * y
    