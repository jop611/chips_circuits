"""
a_star.py

A*-algorithm for pathfinding between gates for a given netlist with use of inadmissable heuristics.


(C) 2020 Teamnaam, Amsterdam, The Netherlands
"""

from code.classes.netlist import Netlist
from code.helpers.helpers import *

class A_Star(object):
    """A_Star is the parent class of multiple algorithms. Heuristics are used to find a valid solution for our case.""" 

    # hardcoded list of all possible directions (north, east, south, west, up, down)
    directions = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
        

    def __init__(self, print_nr, netlist_nr):

        self.netlist = Netlist(print_nr, netlist_nr)
        self.current_coordinate = None
        self.gate_a = None
        self.gate_b = None

        self.x_a = None
        self.y_a = None
        self.z_a = None

        self.x_b = None
        self.y_b = None
        self.z_b = None

        self.min_x = self.netlist.print.boundaries[0][0]
        self.max_x = self.netlist.print.boundaries[1][0]
        self.min_y = self.netlist.print.boundaries[0][1]
        self.max_y = self.netlist.print.boundaries[1][1]
        self.min_z = self.netlist.print.boundaries[0][2]
        self.max_z = self.netlist.print.boundaries[1][2]

        self.origin = None
        self.current_coordinate = None
        self.destination = None


    def valid_move(self, coordinate):
        """
        Checks if a coordinate satisfies all constraints.

        Constraints:
        - The coordinates can not be part of an existing path, 
          unless it is the destination coordinate, which could be in multiple paths.
        - The coordinates can not have been checked for validity before.
        - The coordinates can not be a gate that is not the destination gate.
        - The coordinates can not lie outside the boundaries.

        Input:
        Coordinate; tuple.

        Return: 
        Boolean.
        """

        x = coordinate[0]
        y = coordinate[1]
        z = coordinate[2]
        
        if ((not self.netlist.check_if_path(coordinate) or self.netlist.check_if_gate(coordinate)) and not coordinate in self.paths
            and ((self.netlist.check_if_gate(coordinate) and coordinate == self.destination) or not self.netlist.check_if_gate(coordinate))
            and (self.min_x <= x <= self.max_x) and (self.min_y <= y <= self.max_y) and (self.min_z <= z <= self.max_z)):

            return True
        return False

    
    def calculate_costs(self, coordinates, direction):
        """
        Calculates the cost to move to certain coordinates. Inadmissable heuristics are choses on purpose.

        Input:
        Coordinate, direction; tuples of x-, y-, z-coordinates.
        
        Return:
        cost; integer.
        """

        x = coordinates[0]
        y = coordinates[1]
        z = coordinates[2]

        # manhattan distance to destination coordinates
        cost = abs(self.x_b - x) + abs(self.y_b - y) + abs(self.z_b - z)
        
        # increasing cost if coordinate is close to make it less favourable
        if self.netlist.penalty(coordinates, self.origin, self.destination):
            cost += 1

        # decreasing cost to make upward movement more favourable
        if direction == (0, 0, 1):
            cost -= 2

        cost -= z * 2

        return cost


    def get_coordinates(self, connection):
        """
        Saves coordinates as new variables for readability purposes.
        
        Input:
        Connection; tuple of two gates to be connected.

        Return:
        None.
        """

        self.gate_a = connection[0]
        self.gate_b = connection[1]

        # split gate coordinates into x-, y-, z- coordinates
        self.x_a = self.netlist.print.gates[self.gate_a][0]
        self.y_a = self.netlist.print.gates[self.gate_a][1]
        self.z_a = self.netlist.print.gates[self.gate_a][2]

        self.x_b = self.netlist.print.gates[self.gate_b][0]
        self.y_b = self.netlist.print.gates[self.gate_b][1]
        self.z_b = self.netlist.print.gates[self.gate_b][2]

        # defining the origin & destination coordinates
        self.origin = (self.x_a, self.y_a, self.z_a)
        self.current_coordinate = self.origin
        self.destination = (self.x_b, self.y_b, self.z_b)

    
    def connect(self, connection):
        """
        Connects two gates via an A*-algorithm.

        Input:
        Connection; tuple of two gates to be connected.
        
        Return:
        None.
        """ 
        
        self.get_coordinates(connection)
        priorities = []
        self.paths = {}

        # perform pathfinding until the destination coordinate is reached
        while not self.connected():
            
            current_coordinate = (self.x_a, self.y_a, self.z_a)

            # iterate over directions
            for direction in A_Star.directions:

                # create temporary coordinates
                temp_coordinate = (self.x_a + direction[0], self.y_a + direction[1], self.z_a + direction[2])
                
                if self.valid_move(temp_coordinate): 

                    # save coordinate as 'visited' coordinate    
                    self.paths[temp_coordinate] = current_coordinate
                    cost = self.calculate_costs(temp_coordinate, direction)
                    priorities.append((temp_coordinate, cost))

            # sort options on lowest cost to destination
            priorities.sort(key=lambda coordinate: coordinate[1])

            # update x-, y-, z- coordinates
            if len(priorities) != 0:
                self.x_a = priorities[0][0][0]
                self.y_a = priorities[0][0][1]
                self.z_a = priorities.pop(0)[0][2]

            # remove all succesful paths, move failed connection to front of netlist if destination is unreachable
            else:
                self.netlist.clear()
                self.netlist.netlist.insert(0, self.netlist.netlist.pop(self.netlist.netlist.index(connection)))
                break

        # trace route from destination to origin, convert path to x-, y-, z- lists for visulization
        if self.connected():
            self.netlist.path[connection] = trace(self.paths, (self.x_a, self.y_a, self.z_a))           
            self.netlist.path_plot[connection] = matlib_convert(self.netlist.path[connection])


    def connected(self):
        """Checks if two gates are connected. Returns boolean."""

        if self.x_a == self.x_b and self.y_a == self.y_b and self.z_a == self.z_b:
            return True
        return False
        

    def solved(self):
        """Checks if a netlist has been solved, i.e. if all connections have been made. Returns boolean."""

        for connection in self.netlist.netlist:
            if not connection in self.netlist.path:
                return False
        return True

    
    def run(self):
        """Runs A*-algorithm for pathfinding between gates. Returns None"""

        # iterate until a solution is found, possibly infinitely long for the most complex netlist.
        while not self.solved():
            for connection in self.netlist.netlist:
                self.connect(connection)
        

        self.netlist.count_wires()
        self.netlist.save_result()

        answer = input("Do you wish to plot a 3D image? Y/N: ").upper()

        if answer == "Y":
            plot(self.netlist.print.x_list, self.netlist.print.y_list, self.netlist.print.z_list, self.netlist.print.boundaries, self.netlist.path_plot, self.netlist.length)


