import csv
import matplotlib.pyplot as plt
import numpy as np
from code.classes.netlist import *
from code.algorithms.constraints import *
from visualize import *



def main():
    print_nr = int(input("Print_nr: "))
    netlist_nr = int(input("Netlist_nr: "))
    print()
    print()
    
    

    netlist = Netlist(print_nr, netlist_nr)
    print(netlist.gates)
    for connection in netlist.netlist:
        print()
        netlist.connect(connection)
        print()
    print(netlist.x_list)
    print(netlist.y_list)
    plot(netlist.x_list, netlist.y_list)
    




if __name__ == "__main__":
    main()
    

    
    
