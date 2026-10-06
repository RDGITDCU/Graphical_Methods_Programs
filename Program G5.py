import numpy as np
import mathplotlib.pyplot as plt
from scipy import integrate

def LV(x,y):
    a = 4
    b = 2
    c = 1/3
    d = 1
    dxdt = (a*x) - (b*x*y)
    dydt = (c*x*y) -(d*y)
    