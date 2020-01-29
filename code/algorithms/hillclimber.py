"""
hillclimber.py

Remove and reconnect gates with the use of adjusted admissable heuristics in order to optimize the solutions to their local minima.

(C) 2020 Teamnaam, Amsterdam, The Netherlands
"""

from code.algorithms.a_star import A_Star
from code.helpers.helpers import plot
import json


class HillClimber(A_Star):
    """
    HillClimber is used optimize the existing paths between gates using admissable heuristics.

    Many functions are equal to those of A_Star, therefore A_Star is chosen as the parent class.
    """ 

    def __init__(self, print_nr, netlist_nr, hillclimb_length):
        super(HillClimber, self).__init__(print_nr, netlist_nr)
        self.hillclimb_length = hillclimb_length
        self.previous_length = 0
        self.diff = None


    def calculate_costs(self, coordinate, direction):
        """
        Calculates the cost to move to certain coordinates. 
        Differs from the A_Star calulate_costs() function, as admissable heuristics are choses. 

        Input:
        Coordinate, direction; tuples of x-, y-, z-coordinates.
        
        Return:
        cost; integer.
        """

        x = coordinate[0]
        y = coordinate[1]
        z = coordinate[2]

        # manhattan distance to destination coordinates
        cost = abs(self.x_b - x) + abs(self.y_b - y) + abs(self.z_b - z)
        
        # increasing cost if coordinate is close to make it less favourable
        if self.netlist.penalty(coordinate, self.origin, self.destination):
            cost += 1

        return cost


    def import_result(self, print_nr, netlist_nr, length):
        """
        Imports obtained result in json format from .txt file.

        Input:
        print_nr, netlist_nr, length; strings of numeric values.

        Return:
        None
        """

        # open .txt file
        with open(f'results/a_star/netlist_{netlist_nr}_{length}.txt', newline='') as infile:
            data = json.load(infile)

            # convert connections in list format to tuple format
            for connection in data["paths"]:
                key = (connection[0][0], connection[0][1], connection[0][2])
                self.netlist.path[key] = []

                # convert all coordinates in paths in list format to tuple format
                for coordinate in connection[1]:
                    coordinate_tuple = (coordinate[0], coordinate[1], coordinate[2])
                    self.netlist.path[key].append(coordinate_tuple)

        # count amount of wires
        self.netlist.count_wires()


    def is_optimized(self):
        """Checks if a solution has reached its local minimum. Returns a boolean.""" 

        if self.previous_length == self.netlist.length:
            return True
        return False

        
    def run(self):
        """Runs a hillclimber algorithm, by using an A*-algorithm with admissable heuristics to find a local minimum. Returns None"""

        # import result
        self.import_result(self.netlist.print_nr, self.netlist.netlist_nr, self.hillclimb_length)

        self.netlist.netlist.sort(key=lambda connection: connection[2], reverse=True)

        # keep iterating while the total wirelength is lower than before
        while not self.is_optimized():            
            for connection in self.netlist.netlist:                
                del self.netlist.path[connection]
                self.connect(connection)

            # update wirelengths
            self.previous_length = self.netlist.length           
            self.netlist.count_wires()

        self.netlist.save_result()

        answer = input("Do you wish to plot a 3D image? Y/N: ").upper()

        if answer == "Y":
            plot(self.netlist.print.x_list, self.netlist.print.y_list, self.netlist.print.z_list, self.netlist.print.boundaries, self.netlist.path_plot, self.netlist.length)






