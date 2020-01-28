"""
hillclimber.py

Recreate connections made with A* algorithm with Hillclimber algorithm & opening A* to adjust connections

(C) 2020 Teamname, Amsterdam, The Netherlands
"""

from code.algorithms.a_star_copy import A_star
from code.algorithms.helpers import *
import json


class Hillclimber(A_star):


    def __init__(self, print_nr, netlist_nr):
        super(Hillclimber, self).__init__(print_nr, netlist_nr)
        self.previous_length = 0


    def calculate_costs(self, temp_coordinate, direction):

        temp_x_a = temp_coordinate[0]
        temp_y_a = temp_coordinate[1]
        temp_z_a = temp_coordinate[2]

        cost = abs(self.x_b - temp_x_a) + abs(self.y_b - temp_y_a) + abs(self.z_b - temp_z_a)
        
        # increasing cost if coordinate is close to a wrong gate so that it avoids it
        if self.netlist.penalty(temp_coordinate, self.origin, self.destination):
            cost += 1

        return cost



    def import_result(self, print_nr, netlist_nr):
        """Open A* solution file needed to be shortened"""

        length = input("Lengte van oplossing om te hillclimben: ")
        with open(f'results/print_{print_nr}/a_star/netlist_{netlist_nr}_{length}.txt', newline='') as infile:
            data = json.load(infile)

            # ..
            for connection in data["paths"]:
                key = (connection[0][0], connection[0][1], connection[0][2])
                self.netlist.path[key] = []

                # ..
                for coordinate in connection[1]:
                    coordinate_tuple = (coordinate[0], coordinate[1], coordinate[2])
                    self.netlist.path[key].append(coordinate_tuple)

        self.netlist.score()


    def optimized(self):

        if self.netlist.length > self.previous_length:
            return False
        return True

        
        

    def run(self):
        
        self.import_result(self.netlist.print_nr, self.netlist.netlist_nr)

        while not self.optimized():

            for connection in self.netlist.netlist:
                del self.netlist.path[connection]

                self.connect(connection)
                
            
            self.previous_length = self.netlist.length
            self.netlist.score()

            print(self.netlist.length, self.previous_length)

        # save solution in json format
        self.netlist.save_result()

        



