"""
wat doet deze file

(C) 2020 Teamname, Amsterdam, The Netherlands
"""
import copy
import json

import csv
from code.classes.print import *


class Netlist():
    def __init__(self, print_nr, netlist_nr):
        self.print_nr = print_nr
        self.netlist_nr = netlist_nr
        self.path_plot = {}
        self.path = {}
        self.connections_count = {}

        self.successful_connections = 0
        self.last_index = 0
        self.previous_connection = None
        self.old_netlist = None
        self.old_path = None
        self.successful_connections = []
        self.random_connection = None
        self.removed_path = None
        self.hillclimb = False

        self.lowerbound = 0
        self.chip_occurences = []
        self.connections_sorted = []
        self.connections_count = {}
        self.length = 0
        self.dick = {}
        self.print = Print(print_nr)

        self.netlist = self.load_netlist(print_nr, netlist_nr)
        self.initial_hillclimber_limit = len(self.netlist)
        self.hillclimber_limit = self.initial_hillclimber_limit
        self.original_netlist = copy.deepcopy(self.netlist) 
        # print(self.lowerbound)
       
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

        # highest_connection_count = {}
        # for connection in netlist:
        #     if self.connections_count[connection[0]] > self.connections_count[connection[1]]:
        #         highest_connection_count[connection] = self.connections_count[connection[0]]
        #     else:
        #         highest_connection_count[connection] = self.connections_count[connection[1]]

        
        # netlist.sort(key=lambda connection: (highest_connection_count[connection], (self.connections_count[connection[0]] + self.connections_count[connection[1]]) / 2, -connection[2]), reverse=True)
        netlist.sort(key=lambda connection: connection[2])
        # (self.connections_count[connection[0]] + self.connections_count[connection[1]] / 2),
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

        return coordinate in [path for connection in self.path.values() for path in connection]


    def check_if_chip(self, coordinate):
        """Check if input coordinate is a location of a chip"""

        return coordinate in self.print.chips.values()


    def check_if_right_chip(self, coordinate, destination):
        """Check if input coordinate is destination coordinate"""

        return coordinate == destination

    def score(self):
        """ Amount of connections made """

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

        # if (coordinate[0] + 1, coordinate[1], coordinate[2] - 1) in self.print.chips_locations and (coordinate[0] + 1, coordinate[1], coordinate[2] - 1) != destination and (coordinate[0] + 1, coordinate[1], coordinate[2] - 1) != origin:
        #     return True
        
        # # -x direction
        # if (coordinate[0] - 1, coordinate[1], coordinate[2] - 1) in self.print.chips_locations and (coordinate[0] - 1, coordinate[1], coordinate[2] - 1) != destination and (coordinate[0] - 1, coordinate[1], coordinate[2 - 1]) != origin:
        #     return True

        # # +y direction
        # if (coordinate[0], coordinate[1] + 1, coordinate[2] - 1) in self.print.chips_locations and (coordinate[0], coordinate[1] + 1, coordinate[2] - 1) != destination and (coordinate[0] + 1, coordinate[1], coordinate[2] - 1) != origin:
        #     return True

        # # -y direction
        # if (coordinate[0], coordinate[1] - 1, coordinate[2] - 1) in self.print.chips_locations and (coordinate[0], coordinate[1] - 1, coordinate[2] - 1) != destination and (coordinate[0] + 1, coordinate[1], coordinate[2] - 1) != origin:
        #     return True

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
            if not connection in self.path or self.path[connection] == []:
                return False
        return True
    
    def save_result(self):
        
        # path = {}
        # for connection in self.netlist:
        #     self.path[connection]

        with open(f'results/print_{self.print_nr}/netlist_{self.netlist_nr}_{self.length}.txt', 'w', newline='') as outfile:
            data = {}
            data["netlist"] = self.netlist
            data["paths"] = [] 

            for connection in self.netlist:
                data["paths"].append((connection, self.path[connection]))
                
            json.dump(data, outfile)

        # with open(f'results/print_{self.print_nr}/netlist_{self.netlist_nr}_{self.length}_netlist.csv', 'w', newline='') as csvfile:
        #     writer = csv.writer(csvfile, delimiter=' ')
        #     writer.writerow([self.length])
        #     writer.writerow([self.netlist])

        # with open(f'results/print_{self.print_nr}/netlist_{self.netlist_nr}_{self.length}.csv', 'w', newline='') as csvfile:
        #     fieldnames = ['connection', 'path']
        #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #     # writer.writerow(self.length)
        #     # writer.writerow(self.netlist)
        #     writer.writeheader()
        #     for connection in self.path:
        #         writer.writerow({'connection': connection, 'path': self.path[connection]})
        # return None


    def sortdick(self):
        for connection in self.netlist:
            if connection not in self.dick:
                self.dick[connection] = 0
        
        self.netlist.sort(key=lambda connection: self.dick[connection], reverse=True)
        
        
        return None

    def blocking_path(self, coordinate):

        # if coordinate in [path for connection in self.path.values() for path in connection]:
        #     return connection
        for connection in self.path:
            if coordinate in self.path[connection]:
                return connection
        return None


    def import_result(self):
        with open(f'results/print_{print_nr}/netlist_{netlist_nr}_1.csv', newline='') as infile:
            data = json.load(infile)
            print(data)
            for connection in data["paths"]:
                self.path[connection[0]] = connection[1]
            
        print(self.path)

    
                
                # keep track of amount of occurences of gate in netlist
                # try:
                #     self.connections_count[int(chip_a)] += 1
                # except KeyError:
                #     self.connections_count[int(chip_a)] = 1
                # except ValueError:
                #     pass

                # try:
                #     self.connections_count[int(chip_b)] += 1
                # except KeyError:
                #     self.connections_count[int(chip_b)] = 1
                # except ValueError:
                #     pass

                # try:
                #     manhattan_distance = abs(self.print.chips[int(chip_b)][0] - self.print.chips[int(chip_a)][0]) + abs(self.print.chips[int(chip_b)][1] - self.print.chips[int(chip_a)][1])
                #     netlist.append((int(chip_a), int(chip_b), manhattan_distance))        
                #     self.lowerbound += manhattan_distance
                #     self.chip_occurences.append(int(chip_a))
                #     self.chip_occurences.append(int(chip_b))
                # except ValueError:
                #     pass
            # print(self.path)


        
        
       
        



