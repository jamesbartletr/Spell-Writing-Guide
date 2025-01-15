# ---------File for Defining Spell Bases---------#
# This script provides functions for generating x, y coordinate data
# for various geometric shapes and mathematical functions.

import numpy as np
import math


def polygon(n, radius=1, start_angle=None):
    """
    Generate x, y coordinates for an n-sided polygon.

    Args:
        n (int): Number of sides for the polygon.
        radius (float, optional): Radius of the polygon. Default is 1.
        start_angle (float, optional): Starting angle (in radians) for the first vertex. Default is calculated as π/n.

    Returns:
        tuple: Two NumPy arrays (x, y) containing the coordinates of the polygon's vertices.
    """
    if start_angle is None:
        start_angle = np.pi / n  # Default starting angle
    small_angle = [start_angle + i * 2 * np.pi / n for i in np.arange(1, n + 1)]
    x, y = (radius * np.sin(small_angle), radius * np.cos(small_angle))
    return (x, y)


def line(n):
    """
    Generate x, y coordinates for a horizontal line of n points.

    Args:
        n (int): Number of points for the line.

    Returns:
        tuple: Two NumPy arrays (x, y) for the line's points, where y is always 0.
    """
    x = np.arange(0, n)
    y = np.zeros((1, n))
    return (x, y[0])


def quadratic(n, a=1, b=0, c=0):
    """
    Generate x, y coordinates based on a quadratic function. The function
    alternates x values between positive and negative to create a zigzagging pattern.

    Args:
        n (int): Number of points to generate.
        a (float, optional): Coefficient for the quadratic term (x^2). Default is 1.
        b (float, optional): Coefficient for the linear term (x). Default is 0.
        c (float, optional): Constant term. Default is 0.

    Returns:
        tuple: Two NumPy arrays (x, y) representing the coordinates.
    """
    x = [0]
    while len(x) < n:
        if -x[-1] in x:
            x.append(-x[-1] + 1)
        else:
            x.append(-x[-1])
    x = np.array(x)
    y = a * x ** 2 + b * x + c
    return (x, y)


def circle(n, radius=1, theta0=0, theta1=-np.pi / 2):
    """
    Generate x, y coordinates for a circular arc between two angles (in radians).

    Args:
        n (int): Number of points to generate.
        radius (float, optional): Radius of the circle. Default is 1.
        theta0 (float, optional): Start angle (in radians). Default is 0.
        theta1 (float, optional): End angle (in radians). Default is -π/2.

    Returns:
        tuple: Two NumPy arrays (x, y) for the arc coordinates.
    """
    theta = np.linspace(theta0, theta1, n)
    x = radius * np.cos(theta)
    y = radius * np.sin(theta)
    return (x, y)


def cubic(n, a=0.1, b=0, c=-0.75, d=0):
    """
    Generate x, y coordinates based on a cubic function.

    Args:
        n (int): Number of points to generate.
        a (float, optional): Coefficient for x^3 term. Default is 0.1.
        b (float, optional): Coefficient for x^2 term. Default is 0.
        c (float, optional): Coefficient for the x term. Default is -0.75.
        d (float, optional): Constant term. Default is 0.

    Returns:
        tuple: Two NumPy arrays (x, y) representing the coordinates.
    """
    x = np.arange(-math.floor(n / 2), math.ceil(n / 2))
    y = a * x ** 3 + b * x ** 2 + c * x + d
    return (x, y)


def golden(n, lim=3 * np.pi):
    """
    Generate x, y coordinates for the golden ratio spiral.

    Args:
        n (int): Number of points to generate.
        lim (float, optional): Angular limit for the spiral (in radians). Default is 3π.

    Returns:
        tuple: Two NumPy arrays (x, y) representing the spiral coordinates.
    """
    t = np.linspace(0, lim, n)
    g = (1 + 5 ** 0.5) / 2  # Golden ratio
    f = g ** (t * g / (2 * np.pi))  # Scaling factor
    x = np.cos(t) * f
    y = np.sin(t) * f
    return (x, y)


if __name__ == "__main__":
    # A simple test script to check the module is running
    print("Hello Nerd!")
