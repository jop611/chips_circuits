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
# from code.algorithms.a_star import *
from code.algorithms.hillclimber import *
from visualize import *


def main():
    print_nr = int(input("Print_nr: "))
    netlist_nr = int(input("Netlist_nr: "))
    print()
    print()

    netlist = Netlist(print_nr, netlist_nr)
    # backup = copy.deepcopy(netlist.netlist)
    i = 0
    # netlist.netlist = [(27, 40, 13), (41, 48, 4), (40, 39, 5), (39, 8, 18), (28, 39, 7), (46, 39, 7),
    #             (39, 50, 9), (45, 35, 15), (33, 26, 12), (4, 22, 8), (2, 38, 12), (2, 21, 9), (45, 29, 15), (31, 41, 11), (38, 41, 3), (30, 38, 8), (15, 17, 7), (35, 20, 10), 
    #             (49, 35, 5), (31, 33, 10), (34, 32, 9), (22, 34, 7), (7, 34, 13), (34, 8, 15), (33, 3, 12), (38, 44, 3), (15, 47, 14), (15, 35, 14), (38, 3, 14), (28, 48, 11), 
    #             (35, 3, 12), (28, 37, 7), (47, 30, 10), (17, 11, 6), (49, 3, 17), (13, 6, 6), (6, 18, 7), (6, 42, 12), (50, 13, 19), (13, 37, 12), (2, 14, 9), (13, 10, 5), 
    #             (40,4, 11), (4, 15, 15), (6, 40, 13), (4, 11, 2), (15, 44, 11), (1, 4, 14), (1, 40,25), (2, 12, 7), (48, 45, 10), (23, 45, 23), (26, 18, 2), (12, 11, 14), 
    #             (12, 46, 15), (31, 8, 19), (47, 1, 21), (17, 9, 7), (26, 7, 7), (44, 32, 10), (37, 21, 12), (50, 29, 14), (14, 46, 15), (22, 43, 16), (25, 30, 3), (18, 36, 21), 
    #             (27, 42, 12), (9, 5, 4), (16, 23, 6), (19, 43, 10)]
    # import_result(print_nr, netlist_nr)

    hillclimber(netlist)

        # print("Fail")
    # print(a_star(netlist))
    # print(netlist.netlist)
    # for i in range(10):
    # a_star(netlist)
        # netlist.clear()
        # i += 1
    # while not a_star(netlist):
        # if netlist.last_index > (len(netlist.netlist) / 2):
        #     old_list = copy.deepcopy(netlist.netlist)
        #     for i in range(netlist.last_index):
        #         old_list

        # i += 1

        
        # print(i)
    # a_star(netlist)
    # print("lol")
    # # print(netlist.netlist)
    # print()

    netlist.score()
    print(netlist.netlist)
    print(netlist.length)
    print("Success!!!")
    print(f"Tries: {i}")
    # print()
    # for connection in backup:
    #     try:
    #         pass
    #         # print(netlist.path[connection])
    #     except:
    #         KeyError
    # print()
    # print(len(netlist.path))
    plot(netlist.print.x_list, netlist.print.y_list, netlist.print.z_list, netlist.print.boundaries, netlist.path_plot, netlist.length)

if __name__ == "__main__":
    main()
