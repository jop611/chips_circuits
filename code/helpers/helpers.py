"""
helpers.py

Traces path of a connection and appends coordinates to list used for visualisation.

(C) 2020 Teamname, Amsterdam, The Netherlands
"""


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def trace(paths, destination):
    """
    Traces path from destination to origin.
    
    Input:
    paths; dictionary

    Return:
    List containing tuples of x-, y-, z-coordinates.
    """

    coordinates = destination
    path = [coordinates]
    
    # iterate over keys in dictionary until the path is traced
    while coordinates in paths:
        coordinates = paths[coordinates]
        path.append(coordinates)
    path.reverse()
    return path


def matlib_convert(path):
    """
    Convert tuples of x-, y-, z-coordinates to x-, y-, z-coordinate lists for visualisation via matplotlib
    
    Input:
    path; list containing tuples of x-, y-, z-coordinates.

    Return:
    Tuple of x-, y-, z-coordinate lists.
    """

    x_list = []
    y_list = []
    z_list = []

    for coordinate in path:
        x_list.append(coordinate[0])
        y_list.append(coordinate[1])
        z_list.append(coordinate[2])
    return (x_list, y_list, z_list)


def plot(x_gates, y_gates, z_gates, boundaries, paths, score):
    """
    Plot gates and connections in a 3D grid.
    
    Input:
    x_gates; list of x-coordinates of all gates.
    y_gates; list of y-coordinates of all gates.
    z_gates; list of z-coordinates of all gates.
    boundaries; tuple of x-, y-, z-coordinates.
    paths; dictionary containing all paths between gates.
    score; integer.
    
    Return:
    None
    """

    # create figure with correct axes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.xticks(np.arange(0, boundaries[1][0] + 1, 1))
    plt.yticks(np.arange(0, boundaries[1][1] + 1, 1))
    plt.title(f"Total wire length: {score}")
    ax.set_xlim3d(0, boundaries[1][0], 1)
    ax.set_ylim3d(0, boundaries[1][1], 1)
    ax.set_zlim3d(0, 7)

    # plot all gates
    for m, zlow, zhigh in [('s', 0, 7)]:
        x = x_gates
        y = y_gates
        z = z_gates
        ax.scatter(x, y, z, marker=m)

    # plot all connections
    for connection in paths:
        ax.plot(paths[connection][0], paths[connection][1], paths[connection][2], '-')

    # axis names
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    plt.show()

