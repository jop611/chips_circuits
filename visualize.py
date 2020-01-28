"""
visualize.py

Make visual grid with gates and connections.

(C) 2020 Teamname, Amsterdam, The Netherlands
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np


def plot(x_gates, y_gates, z_gates, boundaries, paths, score):
    """ Load grid with gates and connections """

    #comment
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.xticks(np.arange(0, boundaries[1][0] + 1, 1))
    plt.yticks(np.arange(0, boundaries[1][1] + 1, 1))
    plt.title(f"Total wire length: {score}")

    ax.set_xlim3d(0, boundaries[1][0], 1)
    ax.set_ylim3d(0, boundaries[1][1], 1)
    ax.set_zlim3d(0, 7)


    for m, zlow, zhigh in [('s', 0, 7)]:
        x = x_gates
        y = y_gates
        z = z_gates
        ax.scatter(x, y, z, marker=m)

    # comment
    for connection in paths:
        ax.plot(paths[connection][0], paths[connection][1], paths[connection][2], '-')

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    plt.show()
