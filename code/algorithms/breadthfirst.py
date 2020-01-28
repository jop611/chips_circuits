"""
Breadth.py

Breadth First algorithm for pathfinding between coordinates for given netlist.
Input is the chosen netlist.
Returns Boolean function, True if all connections are made and False if not all connections could be made.

(C) 2020 Teamname, Amsterdam, The Netherlands
"""


from code.algorithms.a_star import A_star
from code.helpers.helpers import *

class BreadthFirst(A_star):

    def connect(self, connection):
    
        self.get_coordinates(connection)
        self.priorities = []
        self.paths = {}

        # perform pathfinding until the destination coordinate is reached
        while not self.connected():
            
            self.current_coordinate = (self.x_a, self.y_a, self.z_a)

            # iterate over all possible directions
            for direction in A_star.directions:

                # create temporary coordinates
                temp_x_a = self.x_a + direction[0]
                temp_y_a = self.y_a + direction[1]
                temp_z_a = self.z_a + direction[2]

                temp_coordinate = (temp_x_a, temp_y_a, temp_z_a)
                
                if self.validate_move(temp_coordinate):

                    # relate new coordinate to old coordinate for tracing
                    self.paths[temp_coordinate] = self.current_coordinate

                    # add temporary to list of valid coordinates
                    self.priorities.append(temp_coordinate)

            # set new x-, y-, z- coordinates if there are valid coordinates to go to
            if len(self.priorities) != 0:
                # move(priorities[0][0])
                self.x_a = self.priorities[0][0]
                self.y_a = self.priorities[0][1]
                self.z_a = self.priorities.pop(0)[2]

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



    def run(self):
        """
        Breadth-First search algorithm for pathfinding between gates
        """

        while not self.solved():
            # self.netlist.clear()

        # iterate over all connections in netlist
            for connection in self.netlist.netlist:

                self.connect(connection)
                
            # count amount of wires used
        self.netlist.score()

        # save solution in json format
        self.netlist.save_result()

        answer = input("Do you wish to plot a 3D image? Y/N: ").upper()

        if answer == "Y":
            plot(self.netlist.print.x_list, self.netlist.print.y_list, self.netlist.print.z_list, self.netlist.print.boundaries, self.netlist.path_plot, self.netlist.length)
