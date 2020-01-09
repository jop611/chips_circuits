import csv
import os, sys
from sys import argv
directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(directory, "code"))
sys.path.append(os.path.join(directory, "code", "classes"))
sys.path.append(os.path.join(directory, "code", "algorithms"))

from netlist import Netlist
from connect import *


def main():
    print_nr = int(input("Print_nr: "))
    netlist_nr = int(input("Netlist_nr: "))
    print()
    print()
    
    netlist = Netlist(print_nr, netlist_nr)
    print(netlist.gates)
    for connection in netlist.connections:
        print()
        netlist.connect(connection)
        print()



if __name__ == "__main__":
    main()
    

    
    
