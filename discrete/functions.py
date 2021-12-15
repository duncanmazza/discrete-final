"""
A few functions used in the convexity_1d.py and convexity_2d.py modules.
"""


import numpy as np


def parabola(a, b, c, x):
    return a*x**2 + b*x + c


def parabola_default(x):
    return parabola(0.5, 0, -2, x)


def parabola_3d(u, v):
    z = 0.5 * u ** 2 + 0.5 * v ** 2
    return np.array([u, v, z])
