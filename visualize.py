import matplotlib.pyplot as plt
import numpy as np
from code.classes.netlist import *

def plot(x_chips, y_chips, boundaries, paths):
    fig = plt.figure()
    score = 0

    for key in paths:
        score += int(key[2])

    plt.axis([boundaries[0][0] - 2, boundaries[1][0] + 2, boundaries[0][1] - 2, boundaries[1][1] + 2])
    plt.xticks(np.arange(0, boundaries[1][0] + 1, 1))
    plt.yticks(np.arange(0, boundaries[1][1] + 1, 1))

    plt.grid(linestyle='dashed', linewidth=1)

    plt.plot(x_chips, y_chips, 'bs')
    plt.title(f'Connections between gates, total wire length: {score}')
    plt.xlabel('x-coordinates -->')
    plt.ylabel('y-coordinates -->')
    
    for connection in paths:

        plt.plot(paths[connection][0], paths[connection][1], '-')   
        

    plt.show()