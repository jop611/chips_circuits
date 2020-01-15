"""
wat doet deze file

(C) 2020 Teamname, Amsterdam, The Netherlands
"""
import csv
from code.classes.print import *


class Netlist():
    def __init__(self, print_nr, netlist_nr):
        self.path_plot = {}
        self.path = {}
        self.print = Print(print_nr)
        self.lowerbound = 0
        self.netlist = self.load_netlist(print_nr, netlist_nr)
        self.length = 0
        print()

    def load_netlist(self, print_nr, netlist_nr):
        """ Load selected netlist """

        netlist = []
        with open(f'gates&netlists/chip_{print_nr}/netlist_{netlist_nr}.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for chip_a, chip_b in reader:
                try:
                    manhattan_distance = abs(self.print.chips[int(chip_b)][0] - self.print.chips[int(chip_a)][0]) + abs(self.print.chips[int(chip_b)][1] - self.print.chips[int(chip_a)][1])
                    netlist.append((int(chip_a), int(chip_b), manhattan_distance))
                    self.lowerbound += manhattan_distance
                except ValueError:
                    pass
            netlist.sort(key=lambda connection: connection[2])
        return netlist

    def check_if_path(self, coordinate):
        """ Check if path has been used """

        for connection in self.path:
            if coordinate in self.path[connection]:
                return True
        return False

    def check_if_chip(self, coordinate):
        """ Check if path contains chip """

        for chip in self.print.chips:
            if coordinate == self.print.chips[chip]:
                return True
        return False

    def check_if_right_chip(self, coordinate, destination):
        """ Check if destination chip has been reached """

        if coordinate == destination:
            return True
        return False

    def score(self):
        """ Amount of conection made """

        for connection in self.path:
            self.length += len(self.path[connection]) - 1


    def penalty(self, coordinate, destination):
        # +x direction
        if (coordinate[0] + 1, coordinate[1], coordinate[2]) in self.print.chips_locations and (coordinate[0] + 1, coordinate[1], coordinate[2]) != destination:
            return True
        
        # -x direction
        if (coordinate[0] - 1, coordinate[1], coordinate[2]) in self.print.chips_locations and (coordinate[0] + 1, coordinate[1], coordinate[2]) != destination:
            return True

        # +y direction
        if (coordinate[0], coordinate[1] + 1, coordinate[2]) in self.print.chips_locations and (coordinate[0] + 1, coordinate[1], coordinate[2]) != destination:
            return True

        # -y direction
        if (coordinate[0], coordinate[1] - 1, coordinate[2]) in self.print.chips_locations and (coordinate[0] + 1, coordinate[1], coordinate[2]) != destination:
            return True

        # -z direction
        if (coordinate[0], coordinate[1], coordinate[2] - 1) in self.print.chips_locations and (coordinate[0] + 1, coordinate[1], coordinate[2]) != destination:
            return True

        # # +x, +y direction
        # if (coordinate[0] + 1, coordinate[1] + 1, coordinate[2]) in self.print.chips_locations and (coordinate[0] + 1, coordinate[1], coordinate[2]) != destination:
        #     return True
        
        # # +x, -y direction
        # if (coordinate[0] + 1, coordinate[1] - 1, coordinate[2]) in self.print.chips_locations and (coordinate[0] + 1, coordinate[1], coordinate[2]) != destination:
        #     return True
        
        # # -x, -y direction
        # if (coordinate[0] - 1, coordinate[1] - 1, coordinate[2]) in self.print.chips_locations and (coordinate[0] + 1, coordinate[1], coordinate[2]) != destination:
        #     return True
        
        # # -x, +y direction
        # if (coordinate[0] - 1, coordinate[1] + 1, coordinate[2]) in self.print.chips_locations and (coordinate[0] + 1, coordinate[1], coordinate[2]) != destination:
        #     return True

            
        return False
