"""
wat doet deze file

(C) 2020 Teamname, Amsterdam, The Netherlands
"""
import csv
import copy
import matplotlib.pyplot as plt
import numpy as np
from code.classes.netlist import *
from code.classes.print import *
from code.algorithms.breadth import *
from visualize import *


def main():
    print_nr = int(input("Print_nr: "))
    netlist_nr = int(input("Netlist_nr: "))
    print()
    print()

    netlist = Netlist(print_nr, netlist_nr)
    
    i = 1
    
    while not bfs(netlist):
        i += 1

   
    netlist.score()
    print(netlist.netlist)
    print(netlist.length)
    print("Success!!!")
    print(f"Tries: {i}")
    
    plot(netlist.print.x_list, netlist.print.y_list, netlist.print.z_list, netlist.print.boundaries, netlist.path_plot, netlist.length)

if __name__ == "__main__":
    main()
