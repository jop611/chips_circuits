"""
wat doet deze file

(C) 2020 Teamname, Amsterdam, The Netherlands
"""
import csv
import matplotlib.pyplot as plt
import numpy as np
from code.classes.netlist import *
from code.classes.print import *
from code.algorithms.constraints import *
from code.algorithms.a_star import *
from visualize import *


def main():
    print_nr = int(input("Print_nr: "))
    netlist_nr = int(input("Netlist_nr: "))
    print()
    print()

    netlist = Netlist(print_nr, netlist_nr)

    print(a_star(netlist))
    print(netlist.netlist)

    netlist.score()
    print(netlist.length)
    plot(netlist.print.x_list, netlist.print.y_list, netlist.print.z_list, netlist.print.boundaries, netlist.path_plot)
<<<<<<< HEAD
    
    
=======

>>>>>>> dff12f09f395c0a1d100fc0d395eb3d85a857a8f
if __name__ == "__main__":
    main()
