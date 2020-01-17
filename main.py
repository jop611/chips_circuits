import csv
import matplotlib.pyplot as plt
import numpy as np
from code.classes.netlist import *
from code.classes.print import *
from code.algorithms.greedy import *

from code.algorithms.breadth import *
from visualize import *


def main():
    print_nr = int(input("Print_nr: "))
    netlist_nr = int(input("Netlist_nr: "))
    print()
    print()
    
    

    netlist = Netlist(print_nr, netlist_nr)
    print(netlist.print.chips)
   
    print()
    greedy(netlist)
    print()
    # print(netlist.print.x_list)
    # print(netlist.print.y_list)
    netlist.score()
    while not bfs(netlist):
        pass
    plot(netlist.print.x_list, netlist.print.y_list, netlist.print.z_list, netlist.print.boundaries, netlist.path_plot, netlist.length)
    




if __name__ == "__main__":
    main()
    

    
    
