"""
netlist.py

Loading the netlist, initializing lists and dictionaries and some helper functions

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
        self.tries = 1
        self.chip_occurences = []
        self.connections_count = {}
        self.length = 0
        self.print = Print(print_nr)
        self.netlist = self.load_netlist(print_nr, netlist_nr)


    def load_netlist(self, print_nr, netlist_nr):
        """Load selected netlist"""

        netlist = []
        with open(f'gates&netlists/chip_{print_nr}/netlist_{netlist_nr}.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for chip_a, chip_b in reader:

                # keep track of amount of occurences of a gate in netlist
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
                    self.chip_occurences.append(int(chip_a))
                    self.chip_occurences.append(int(chip_b))
                except ValueError:
                    pass

        highest_connection_count = {}

        # assign highest amount of occurrences of either gate to a connection
        for connection in netlist:
            if self.connections_count[connection[0]] > self.connections_count[connection[1]]:
                highest_connection_count[connection] = self.connections_count[connection[0]]
            else:
                highest_connection_count[connection] = self.connections_count[connection[1]]

        # Sort list on highest amount of connections of either gates
        netlist.sort(key=lambda connection: (highest_connection_count[connection], (self.connections_count[connection[0]] + self.connections_count[connection[1]]) / 2, -connection[2]), reverse=True)

        return netlist


    def check_if_path(self, coordinate):
        """Check if path lies in existing path"""

        return coordinate in [path for connection in self.path.values() for path in connection]


    def check_if_chip(self, coordinate):
        """Check if input coordinate is a location of a chip"""

        return coordinate in self.print.chips.values()


    def score(self):
        """Count amount of connections made"""

        self.length = 0
        for connection in self.path:
            self.length += (len(self.path[connection]) - 1)


    def penalty(self, coordinate, origin, destination):
        """Determine if a coordinate is adjacent to a gate that it does not originate from, and is not its destination"""

        x = coordinate[0]
        y = coordinate[1]
        z = coordinate[2]

        north = (x, y + 1, z)
        east = (x + 1, y, z)
        south = (x, y - 1, z)
        west = (x - 1, y, z)
        down = (x, y, z - 1)

        if ((east in self.print.chips_locations and east != destination and east != origin)
           or (west in self.print.chips_locations and west != destination and west != origin)
           or (north in self.print.chips_locations and north != destination and north != origin)
           or (south in self.print.chips_locations and south != destination and south != origin)
           or (down in self.print.chips_locations and down != destination and down != origin)):
            return True

        return False


    def clear(self):
        """Clear all paths when connection making gets stuck"""

        self.path_plot.clear()
        self.path.clear()
        self.length = 0
        return None


    # def solved(self):
    #     for connection in self.netlist:
    #         if not connection in self.path:
    #             return False
    #     return True

    def save_result(self):
        """Save connections of succesfull netlist into csv file"""

        with open(f'results/print_{self.print_nr}/a_star/netlist_{self.netlist_nr}_{self.length}.txt', 'w', newline='') as outfile:
            data = {}
            data["netlist"] = self.netlist
            data["paths"] = []
            data["heuristiek"] = "gesorteerd op hoogst aantal connecties dat een van beide gates heeft in de netlist, daarna op gemiddeld aantal connecties in netlist, daarna op manhattan_distance, cost = manhattan_distance - 2 if (0, 0, 1) - 2 * temp_z + 1 if penalty()"
            data["length"] = self.length
            data["tries"] = self.tries

            for connection in self.netlist:
                data["paths"].append((connection, self.path[connection]))

            json.dump(data, outfile)
