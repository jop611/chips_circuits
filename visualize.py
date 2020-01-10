import matplotlib.pyplot as plt
import numpy as np
from code.classes.netlist import *

def plot(x_chips, y_chips, paths):
    fig = plt.figure()

    # grid traits print #1
    plt.axis([-2, 19, -2, 14])
    plt.xticks(np.arange(0, 18, 1))
    plt.yticks(np.arange(0, 13, 1))

    plt.grid(linestyle='dashed', linewidth=1)

    plt.plot(x_chips, y_chips, 'bs')
    
    for connection in paths:

        plt.plot(paths[connection][0], paths[connection][1], '-')   
        

    plt.show()