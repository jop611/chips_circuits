from mpl_toolkits.mplot3d import Axes3D

import matplotlib.pyplot as plt
import numpy as np
from code.classes.netlist import *

def plot(x_chips, y_chips, z_chips, boundaries, paths):
    # fig = plt.figure()
    # score = 0

    # for key in paths:
    #     score += int(key[2])

    # plt.axis([boundaries[0][0] - 2, boundaries[1][0] + 2, boundaries[0][1] - 2, boundaries[1][1] + 2])
    # plt.xticks(np.arange(0, boundaries[1][0] + 1, 1))
    # plt.yticks(np.arange(0, boundaries[1][1] + 1, 1))

    # plt.grid(linestyle='dashed', linewidth=1)

    # plt.plot(x_chips, y_chips, 'bs')
    # plt.title(f'Connections between gates, total wire length: {score}')
    # plt.xlabel('x-coordinates -->')
    # plt.ylabel('y-coordinates -->')
    
    # for connection in paths:

    #     plt.plot(paths[connection][0], paths[connection][1], '-')   
        

    # plt.show()

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    plt.xticks(np.arange(0, boundaries[1][0] + 1, 1))
    plt.yticks(np.arange(0, boundaries[1][1] + 1, 1))
    # plt.zticks(np.arrange(0, 7))
    # plt.zticks(np.arange(0, boundaries[1][2] + 1, 1))
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
    
    for connection in paths:
        
        ax.plot(paths[connection][0], paths[connection][1], paths[connection][2], '-')   
        

    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')

    plt.show()