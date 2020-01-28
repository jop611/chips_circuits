"""
breadthfirst.py

Breadth First algorithm for pathfinding between gates for a given netlist.


(C) 2020 Teamname, Amsterdam, The Netherlands
"""

from code.algorithms.a_star import A_Star
from code.helpers.helpers import *


class BreadthFirst(A_Star):
    """
    BreadthFirst is a subclass of A_Star used to pathfind between gates without using heuristics.

    Many functions are equal to those of A_Star, therefore A_Star is chosen as the parent class.
    """ 

    def connect(self, connection):
        """
        Connects two gates via a Breadth-first search-algorithm.
        Differs from the A_Star connect() function as the cost system is absent.

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
            
            self.current_coordinate = (self.x_a, self.y_a, self.z_a)

            # iterate over directions
            for direction in A_Star.directions:

                # create temporary coordinates
                temp_coordinate = (self.x_a + direction[0], self.y_a + direction[1], self.z_a + direction[2])

                
                if self.valid_move(temp_coordinate):     
                    
                    # save coordinate as 'visited' coordinate               
                    self.paths[temp_coordinate] = self.current_coordinate
                    priorities.append(temp_coordinate)

            # update x-, y-, z- coordinates
            if len(priorities) != 0:
                self.x_a = priorities[0][0]
                self.y_a = priorities[0][1]
                self.z_a = priorities.pop(0)[2]

            # remove all succesful paths, move failed connection to front of netlist if destination is unreachable
            else:
                self.netlist.clear()
                self.netlist.netlist.insert(0, self.netlist.netlist.pop(self.netlist.netlist.index(connection)))
                break

        # trace route from destination to origin, convert path to x-, y-, z- lists for visulization
        if self.connected():
            self.netlist.path[connection] = trace(self.paths, (self.x_a, self.y_a, self.z_a))
            self.netlist.path_plot[connection]  = matlib_convert(self.netlist.path[connection])


    def run(self):
        """
        Runs Breadth-First search algorithm for pathfinding between gates.

        Return:
        None
        """

        while not self.solved():

        # iterate over all connections in netlist
            for connection in self.netlist.netlist:
                self.connect(connection)
                
        # count amount of wires used
        self.netlist.score()

        # save solution
        self.netlist.save_result()

        answer = input("Do you wish to plot a 3D image? Y/N: ").upper()

        if answer == "Y":
            plot(self.netlist.print.x_list, self.netlist.print.y_list, self.netlist.print.z_list, self.netlist.print.boundaries, self.netlist.path_plot, self.netlist.length)
