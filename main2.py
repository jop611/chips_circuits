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
from code.algorithms.a_star_random import *
from visualize import *


def main():
    print_nr = int(input("Print_nr: "))
    netlist_nr = int(input("Netlist_nr: "))
    print()
    print()

    netlist = Netlist(print_nr, netlist_nr)
    backup = copy.deepcopy(netlist.netlist)
    i = 0
    while not (a_star(netlist)):
        i += 1
        # print("Fail")
    # print(a_star(netlist))
    # print(netlist.netlist)
    
    netlist.score()
    print(netlist.length)
    print("Success!!!")
    print(f"Tries: {i}")
    print()
    for connection in backup:
        print(netlist.path[connection])
    print()
    print(len(netlist.path))
    plot(netlist.print.x_list, netlist.print.y_list, netlist.print.z_list, netlist.print.boundaries, netlist.path_plot, netlist.length)

if __name__ == "__main__":
    main()
