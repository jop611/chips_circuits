import matplotlib.pyplot as plt
import numpy as np

def plot(x_list, y_list):
    fig = plt.figure()
    plt.axis([-1, 18, -1, 13])
    plt.xticks(np.arange(-1, 18, 1))
    plt.yticks(np.arange(-1, 13, 1))
    plt.grid(linestyle='dashed', linewidth=1)


    plt.plot(x_list, y_list, 'bs')
            


    plt.show()