import csv

from code.classes.netlist import *



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
    

    
    
