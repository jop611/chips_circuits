"""
netlist.py

Loading the netlist, initializing lists and dictionaries and some helper functions.

(C) 2020 Teamname, Amsterdam, The Netherlands
"""

import json
import csv
from code.classes.print import Print


class Netlist():
    def __init__(self, print_nr, netlist_nr):
        self.print_nr = print_nr
        self.netlist_nr = netlist_nr
        self.path_plot = {}
        self.path = {}
        self.connections_count = {}
        self.tries = 1
        self.connections_count = {}
        self.length = 0
        self.print = Print(print_nr)
        self.netlist = self.load_netlist(print_nr, netlist_nr)


    def load_netlist(self, print_nr, netlist_nr):
        """
        Load netlist from a .csv file.
        
        Input:
        print_nr, netlist_nr; strings of numeric values.

        Return:
        List containing tuples of all connections in the netlist.
        """

        netlist = []
        # open .csv file
        with open(f'gates&netlists/chip_{print_nr}/netlist_{netlist_nr}.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for gate_a, gate_b in reader:
              
                
                try:
                    # keep track how many times a gate is present in the netlist
                    if int(gate_a) in self.connections_count:
                        self.connections_count[int(gate_a)] += 1
                    else:
                        self.connections_count[int(gate_a)] = 1
                    
                    if int(gate_b) in self.connections_count:
                        self.connections_count[int(gate_b)] += 1
                    else:
                        self.connections_count[int(gate_b)] = 1


                    # reassignment of variables for readability purposes
                    x_origin = self.print.gates[int(gate_a)][0]
                    y_origin = self.print.gates[int(gate_a)][1]
                    x_destination = self.print.gates[int(gate_b)][0]
                    y_destination = self.print.gates[int(gate_b)][1]
                    
                    # save connection
                    manhattan_distance = abs(x_destination - x_origin) + abs(y_destination - y_origin)
                    netlist.append((int(gate_a), int(gate_b), manhattan_distance))
                except ValueError:
                    pass

        highest_connection_count = {}

        # assign highest amount of occurrences of either gate to a connection for sorting
        for connection in netlist:
            if self.connections_count[connection[0]] > self.connections_count[connection[1]]:
                highest_connection_count[connection] = self.connections_count[connection[0]]
            else:
                highest_connection_count[connection] = self.connections_count[connection[1]]

        # sort list on respectively the highest amount of connections of either gates, 
        # average amount of connections, and lowest manhattan distance between gates
        netlist.sort(key=lambda connection: (highest_connection_count[connection], (self.connections_count[connection[0]] + self.connections_count[connection[1]]) / 2, -connection[2]), reverse=True)
        return netlist


    def check_if_path(self, coordinate):
        """Check if coordinates are present in an existing path. Returns a boolean."""

        return coordinate in [path for connection in self.path.values() for path in connection]


    def check_if_gate(self, coordinate):
        """Check if coordinates are the location of a gate. Returns a boolean."""

        return coordinate in self.print.gates.values()


    def count_wires(self):
        """Counts connections between coordinates are made, i.e. how many wires are used. Returns self.lenght; integer."""

        self.length = 0
        for connection in self.path:
            self.length += (len(self.path[connection]) - 1)
        return self.length


    def penalty(self, coordinates, origin, destination):
        """
        Determine if a coordinate is adjacent to a gate that it does not originate from, and is not its destination
        
        Input:
        Coordinates, origin, destination; tuples x-, y-, z-coordinates

        Return:
        Boolean
        """

        # reassignment of variables for readability purposes
        x = coordinates[0]
        y = coordinates[1]
        z = coordinates[2]        
        north = (x, y + 1, z)
        east = (x + 1, y, z)
        south = (x, y - 1, z)
        west = (x - 1, y, z)
        down = (x, y, z - 1)

        if ((east in self.print.gates_locations and east != destination and east != origin)
           or (west in self.print.gates_locations and west != destination and west != origin)
           or (north in self.print.gates_locations and north != destination and north != origin)
           or (south in self.print.gates_locations and south != destination and south != origin)
           or (down in self.print.gates_locations and down != destination and down != origin)):
            return True
        return False


    def clear(self):
        """Clear paths, related visualisation data, and total wirelength when connection making gets stuck. Returns None"""

        self.path_plot.clear()
        self.path.clear()
        self.length = 0


    def save_result(self):
        """Save connections of succesful netlist in json format into .txt file. Returns None."""

        # open .csv file
        with open(f'results/hillclimb/manhattan_distance_lang_eerst_penalty/netlist_{self.netlist_nr}_{self.length}.txt', 'w', newline='') as outfile:
            data = {}
            data["netlist"] = self.netlist
            data["paths"] = []
            data["length"] = self.length
            data["tries"] = self.tries

            # iterate over all connections
            for connection in self.netlist:
                data["paths"].append((connection, self.path[connection]))

            json.dump(data, outfile)
