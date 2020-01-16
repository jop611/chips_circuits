"""
Make visual grid with chips and connections

(C) 2020 Teamname, Amsterdam, The Netherlands
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from code.classes.netlist import *

def plot(x_chips, y_chips, z_chips, boundaries, paths):
    """ Load grid with chips and connections """

    #comment
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.xticks(np.arange(0, boundaries[1][0] + 1, 1))
    plt.yticks(np.arange(0, boundaries[1][1] + 1, 1))

    ax.set_xlim3d(0, boundaries[1][0], 1)
    ax.set_ylim3d(0, boundaries[1][1], 1)
    ax.set_zlim3d(0, 7)

    # For each set of style and range settings, plot n random points in the box
    # defined by x in [23, 32], y in [0, 100], z in [zlow, zhigh].
    for m, zlow, zhigh in [('s', 0, 7)]:
        xs = x_chips
        ys = y_chips
        zs = z_chips
        ax.scatter(xs, ys, zs, marker=m)

    # comment
    for connection in paths:
        ax.plot(paths[connection][0], paths[connection][1], paths[connection][2], '-')

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    plt.show()
