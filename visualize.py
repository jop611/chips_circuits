import matplotlib.pyplot as plt
import numpy as np
from code.classes.netlist import *

def plot(x_list, y_list):
    fig = plt.figure()

    # grid traits print #1
    plt.axis([-1, 18, -1, 13])
    plt.xticks(np.arange(0, 17, 1))
    plt.yticks(np.arange(0, 12, 1))
    plt.grid(linestyle='dashed', linewidth=1)


    plt.plot(x_list, y_list, '-o')
            


    plt.show()