import csv
import matplotlib.pyplot as plt
import numpy as np
from code.classes.netlist import *
from code.classes.print import *
from code.algorithms.constraints import *
from visualize import *


def main():
    print_nr = int(input("Print_nr: "))
    netlist_nr = int(input("Netlist_nr: "))
    print()
    print()
    
    

    netlist = Netlist(print_nr, netlist_nr)
    print(netlist.print.chips)
    for connection in netlist.netlist:
        print()
        netlist.connect(connection)
        print()
    print(netlist.print.x_list)
    print(netlist.print.y_list)
    plot(netlist.print.x_list, netlist.print.y_list)
    




if __name__ == "__main__":
    main()
    

    
    
