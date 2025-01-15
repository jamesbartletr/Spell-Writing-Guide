import numpy as np
import math


# Functions for drawing lines and circles connecting two points:
def centre_circle(P, Q, thetas=None):
    """
    Draws a connecting circular arc or full circle between two points using
    the arithmetic mean of the two points as the circle's center.

    Parameters:
        P (tuple): Coordinates of the first point (x1, y1).
        Q (tuple): Coordinates of the second point (x2, y2).
        thetas (str, optional): If "Full", the function generates a full circle,
                                otherwise generates an arc between the points.

    Returns:
        tuple: Two arrays (X2, Y2) representing the x and y coordinates
               of the circle or arc.
    """
    x1, y1 = P
    x2, y2 = Q

    # Calculate the center (a, b) and radius (r)
    a = (x1 + x2) / 2
    b = (y1 + y2) / 2
    r = np.sqrt((a - x1) ** 2 + (b - y1) ** 2)

    # Generate angles for the arc or full circle
    if thetas == "Full":
        theta = np.linspace(0, 2 * np.pi, 150)
    else:
        theta0 = math.atan2(y1 - b, x1 - a)
        theta1 = math.atan2(y2 - b, x2 - a)

        # Ensure correct arc direction
        if y2 < y1:
            theta0, theta1 = theta1 + np.pi, theta0 + np.pi
        theta = np.linspace(theta0, theta1, 150)

    # Compute circle coordinates
    X2 = r * np.cos(theta) + a
    Y2 = r * np.sin(theta) + b
    return (X2, Y2)


def non_centre_circle(P, Q, b, thetas=None):
    """
    Draws a connecting circular arc or full circle between two points
    with a center offset by 'b' from the arithmetic mean of the points.

    Parameters:
        P (tuple): Coordinates of the first point (x1, y1).
        Q (tuple): Coordinates of the second point (x2, y2).
        b (float): Offset for the center in the y-direction.
        thetas (str, optional): If "Full", the function generates a full circle,
                                otherwise generates an arc between the points.

    Returns:
        tuple: Two arrays (X, Y) representing the x and y coordinates
               of the circle or arc.
    """
    x1, y1 = P
    x2, y2 = Q
    b2 = -b

    # Calculate potential centers and radius
    delta = x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2
    a = (delta - 2 * (y1 - y2) * b) / (2 * (x1 - x2))
    a2 = (delta - 2 * (y1 - y2) * b2) / (2 * (x1 - x2))
    r = np.sqrt((x1 - a) ** 2 + (y1 - b) ** 2)
    r2 = np.sqrt((x1 - a2) ** 2 + (y1 - b2) ** 2)

    # Select the smaller arc and corresponding center
    if r2 <= r:
        a, b, r = a2, b2, r2

    # Generate angles for the arc or full circle
    if thetas == "Full":
        theta = np.linspace(0, 2 * np.pi, 150)
    else:
        theta0 = math.atan2(y1 - b, x1 - a)
        theta1 = math.atan2(y2 - b, x2 - a)

        # Ensure correct arc direction
        theta02, theta12 = theta0, theta1
        while theta1 < theta0:
            theta0 -= 2 * np.pi
        while theta02 < theta12:
            theta12 -= 2 * np.pi

        arc1 = r * (theta1 - theta0)
        arc2 = r * (theta02 - theta12)

        # Select the smaller arc or based on center offset
        if arc1 < arc2 or np.sqrt(b ** 2) < 1:
            theta = np.linspace(theta1, theta0, 150)
        else:
            theta = np.linspace(theta02, theta12, 150)

    # Compute circle coordinates
    X = r * np.cos(theta) + a
    Y = r * np.sin(theta) + b
    return (X, Y)


def straight(P, Q):
    """
    Creates a straight line connecting two points.

    Parameters:
        P (tuple): Coordinates of the first point (x1, y1).
        Q (tuple): Coordinates of the second point (x2, y2).

    Returns:
        tuple: Two lists (X, Y) representing the x and y coordinates
               of the straight line.
    """
    X = [P[0], Q[0]]
    Y = [P[1], Q[1]]
    return (X, Y)
