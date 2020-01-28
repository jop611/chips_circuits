"""
a_star.py

A*-algorithm for pathfinding between coordinates for given netlist.
Returns Boolean function.

(C) 2020 Teamname, Amsterdam, The Netherlands
"""

from code.classes.netlist import Netlist
from code.algorithms.helpers import *

class A_star(object):

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


    def validate_move(self, temp_coordinate):

        temp_x_a = temp_coordinate[0]
        temp_y_a = temp_coordinate[1]
        temp_z_a = temp_coordinate[2]

        # verify that temporary coordinates are valid coordinates
        if ((not self.netlist.check_if_path(temp_coordinate) or self.netlist.check_if_gate(temp_coordinate)) and not temp_coordinate in self.paths
            and ((self.netlist.check_if_gate(temp_coordinate) and temp_coordinate == self.destination) or not self.netlist.check_if_gate(temp_coordinate))
            and (not temp_x_a < self.min_x and not temp_x_a > self.max_x
                and not temp_y_a < self.min_y and not temp_y_a > self.max_y
                and not temp_z_a < self.min_z and not temp_z_a > self.max_z)):

            return True
        return False

    
    def calculate_costs(self, temp_coordinate, direction):

        temp_x_a = temp_coordinate[0]
        temp_y_a = temp_coordinate[1]
        temp_z_a = temp_coordinate[2]

        cost = abs(self.x_b - temp_x_a) + abs(self.y_b - temp_y_a) + abs(self.z_b - temp_z_a)
        
        # increasing cost if coordinate is close to a wrong gate so that it avoids it
        if self.netlist.penalty(temp_coordinate, self.origin, self.destination):
            cost += 1

        if direction == (0, 0, 1):
            cost -= 2
        cost -= temp_z_a * 2

        return cost


    def get_coordinates(self, connection):


        self.gate_a = connection[0]
        self.gate_b = connection[1]

        # gate coordinates split into x-, y-, z- coordinates
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
        
        self.get_coordinates(connection)
        self.priorities = []
        self.paths = {}

        # perform pathfinding until the destination coordinate is reached
        while self.x_a != self.x_b or self.y_a != self.y_b or self.z_a != self.z_b:
            
            self.current_coordinate = (self.x_a, self.y_a, self.z_a)

            # iterate over all possible directions
            for direction in A_star.directions:

                # create temporary coordinates
                temp_x_a = self.x_a + direction[0]
                temp_y_a = self.y_a + direction[1]
                temp_z_a = self.z_a + direction[2]

                temp_coordinate = (temp_x_a, temp_y_a, temp_z_a)
                
                if self.validate_move(temp_coordinate):

                    cost = self.calculate_costs(temp_coordinate, direction)

                    # relate new coordinate to old coordinate for tracing
                    self.paths[temp_coordinate] = self.current_coordinate

                    # add temporary to list of valid coordinates
                    self.priorities.append((temp_coordinate, cost))

            # sort valid coordinates on lowest cost to destination
            self.priorities.sort(key=lambda coordinate: coordinate[1])

            # set new x-, y-, z- coordinates if there are valid coordinates to go to
            if len(self.priorities) != 0:
                # move(priorities[0][0])
                self.x_a = self.priorities[0][0][0]
                self.y_a = self.priorities[0][0][1]
                self.z_a = self.priorities.pop(0)[0][2]

            # remove all succesful paths, move failed connection to front of netlist
            else:
                self.netlist.clear()
                self.netlist.netlist.insert(0, self.netlist.netlist.pop(self.netlist.netlist.index(connection)))
                break

    
        if self.connected():
            # trace route from destination to origin
            self.netlist.path[connection] = trace(self.paths, (self.x_a, self.y_a, self.z_a))

            # convert path coordinates to x-, y-, z- coordinate lists for visualization via matplotlib
            self.netlist.path_plot[connection]  = matlib_convert(self.netlist.path[connection])


    def connected(self):
        if self.x_a == self.x_b and self.y_a == self.y_b and self.z_a == self.z_b:
            return True
        return False
        


    def solved(self):
        for connection in self.netlist.netlist:
            if not connection in self.netlist.path:
                return False
        return True

    
    def run(self):
        """
        A*-algorithm for pathfinding between coordinates
        """

        while not self.solved():
            self.netlist.clear()
        # iterate over all connections in netlist
            for connection in self.netlist.netlist:

                self.connect(connection)
                
            # count amount of wires used
        self.netlist.score()

        # save solution in json format
        self.netlist.save_result()


