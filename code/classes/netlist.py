"""
wat doet deze file

(C) 2020 Teamname, Amsterdam, The Netherlands
"""

import csv
from code.classes.print import *


class Netlist():
    def __init__(self, print_nr, netlist_nr):
        self.print_nr = print_nr
        self.netlist_nr = netlist_nr
        self.path_plot = {}
        self.path = {}
        self.connections_count = {}
        
        self.lowerbound = 0
        self.chip_occurences = []
        self.connections_sorted = []
        self.connections_count = {}
        self.length = 0
        self.print = Print(print_nr)
        self.netlist = self.load_netlist(print_nr, netlist_nr)
       
        # self.count_connections()

        print()

    def load_netlist(self, print_nr, netlist_nr):
        """ Load selected netlist """

        netlist = []
        with open(f'gates&netlists/chip_{print_nr}/netlist_{netlist_nr}.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for chip_a, chip_b in reader:

                # keep track of amount of occurences of gate in netlist
                try:
                    self.connections_count[int(chip_a)] += 1
                except KeyError:
                    self.connections_count[int(chip_a)] = 1
                except ValueError:
                    pass

                try:
                    self.connections_count[int(chip_b)] += 1
                except KeyError:
                    self.connections_count[int(chip_b)] = 1
                except ValueError:
                    pass

                try:
                    manhattan_distance = abs(self.print.chips[int(chip_b)][0] - self.print.chips[int(chip_a)][0]) + abs(self.print.chips[int(chip_b)][1] - self.print.chips[int(chip_a)][1])
                    netlist.append((int(chip_a), int(chip_b), manhattan_distance))        
                    self.lowerbound += manhattan_distance
                    self.chip_occurences.append(int(chip_a))
                    self.chip_occurences.append(int(chip_b))
                except ValueError:
                    pass
        netlist.sort(key=lambda connection: ((-self.connections_count[connection[0]] - self.connections_count[connection[1]])/2, connection[2]))
        # for chip in self.connections_count:
        #     if self.connections_count[chip] == 5:
        #         for connection in netlist:
        #             if connection[0] == chip or connection[1] == chip:
        #                 netlist.remove(connection)                  
        #                 netlist.insert(0, connection)
        # print
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

        self.length = 0
        for connection in self.path:
            self.length += (len(self.path[connection]) - 1)


    def penalty(self, coordinate, origin, destination):
        # +x direction
        if (coordinate[0] + 1, coordinate[1], coordinate[2]) in self.print.chips_locations and (coordinate[0] + 1, coordinate[1], coordinate[2]) != destination and (coordinate[0] + 1, coordinate[1], coordinate[2]) != origin:
            return True
        
        # -x direction
        if (coordinate[0] - 1, coordinate[1], coordinate[2]) in self.print.chips_locations and (coordinate[0] - 1, coordinate[1], coordinate[2]) != destination and (coordinate[0] - 1, coordinate[1], coordinate[2]) != origin:
            return True

        # +y direction
        if (coordinate[0], coordinate[1] + 1, coordinate[2]) in self.print.chips_locations and (coordinate[0], coordinate[1] + 1, coordinate[2]) != destination and (coordinate[0] + 1, coordinate[1], coordinate[2]) != origin:
            return True

        # -y direction
        if (coordinate[0], coordinate[1] - 1, coordinate[2]) in self.print.chips_locations and (coordinate[0], coordinate[1] - 1, coordinate[2]) != destination and (coordinate[0] + 1, coordinate[1], coordinate[2]) != origin:
            return True

        # -z direction
        if (coordinate[0], coordinate[1], coordinate[2] - 1) in self.print.chips_locations and (coordinate[0], coordinate[1], coordinate[2] - 1) != destination and (coordinate[0], coordinate[1], coordinate[2] - 1) != origin:
            return True

        if (coordinate[0] + 1, coordinate[1], coordinate[2] - 1) in self.print.chips_locations and (coordinate[0] + 1, coordinate[1], coordinate[2] - 1) != destination and (coordinate[0] + 1, coordinate[1], coordinate[2] - 1) != origin:
            return True
        
        # -x direction
        if (coordinate[0] - 1, coordinate[1], coordinate[2] - 1) in self.print.chips_locations and (coordinate[0] - 1, coordinate[1], coordinate[2] - 1) != destination and (coordinate[0] - 1, coordinate[1], coordinate[2 - 1]) != origin:
            return True

        # +y direction
        if (coordinate[0], coordinate[1] + 1, coordinate[2] - 1) in self.print.chips_locations and (coordinate[0], coordinate[1] + 1, coordinate[2] - 1) != destination and (coordinate[0] + 1, coordinate[1], coordinate[2] - 1) != origin:
            return True

        # -y direction
        if (coordinate[0], coordinate[1] - 1, coordinate[2] - 1) in self.print.chips_locations and (coordinate[0], coordinate[1] - 1, coordinate[2] - 1) != destination and (coordinate[0] + 1, coordinate[1], coordinate[2] - 1) != origin:
            return True

        # # +x, +y direction
        # if (coordinate[0] + 1, coordinate[1] + 1, coordinate[2]) in self.print.chips_locations and (coordinate[0] + 1, coordinate[1] + 1, coordinate[2]) != destination and (coordinate[0] + 1, coordinate[1] + 1, coordinate[2]) != origin:
        #     return True
        
        # # +x, -y direction
        # if (coordinate[0] + 1, coordinate[1] - 1, coordinate[2]) in self.print.chips_locations and (coordinate[0] + 1, coordinate[1] - 1, coordinate[2]) != destination and (coordinate[0] + 1, coordinate[1] - 1, coordinate[2]) != origin: 
        #     return True
        
        # # -x, -y direction
        # if (coordinate[0] - 1, coordinate[1] - 1, coordinate[2]) in self.print.chips_locations and (coordinate[0] - 1, coordinate[1] - 1, coordinate[2]) != destination and (coordinate[0] - 1, coordinate[1] - 1, coordinate[2]) != origin:
        #     return True
        
        # # -x, +y direction
        # if (coordinate[0] - 1, coordinate[1] + 1, coordinate[2]) in self.print.chips_locations and (coordinate[0] - 1, coordinate[1] + 1, coordinate[2]) != destination and (coordinate[0] - 1, coordinate[1] + 1, coordinate[2]) != origin:
        #     return True

            
        return False

    # def count_connections(self):
    #     for i in range(self.print.chip_count):
    #         # self.chip_occurences.count(i + 1)
    #         print(f"{i + 1}: {self.chip_occurences.count(i + 1)}")
    #         self.connections_count[i + 1] = self.chip_occurences.count(i + 1)
            
    #     return None

    
    def clear(self):
        self.path_plot.clear()
        self.path.clear()
        self.length = 0
        return None
    

    def test(self):
        for connection in self.netlist:
            try:
                print(self.path[connection])
            except KeyError:
                print("Shit toch niet goed")
    
    def save_result(self):
        with open(f'results/print_{self.print_nr}/netlist_{self.netlist_nr}_{self.length}.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=' ')
            writer.writerow([self.length])
            writer.writerow([self.netlist])

        with open(f'results/print_{self.print_nr}/netlist_{self.netlist_nr}_{self.length}.csv', 'a', newline='') as csvfile:
            fieldnames = ['connection', 'path']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            # writer.writerow(self.length)
            # writer.writerow(self.netlist)
            writer.writeheader()
            for connection in self.netlist:
                writer.writerow({'connection': connection, 'path': self.path[connection]})
        return None


        
        
       
        



