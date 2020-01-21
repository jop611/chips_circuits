"""
A*-algorithm for pathfinding between coordinates
"""

import copy
from code.classes.netlist import *
from code.classes.print import *
from code.algorithms.random import *
from code.algorithms.helpers import *


def a_star(netlist):
    """ """
    # hardcoded list of all possible directions (north, east, south, west, up, down)
    directions = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    i = 0

    netlist_copy = copy.deepcopy(netlist.netlist)
    
    # iterate over all connections in netlist
    while len(netlist_copy) > 0:        
        connection = randomize(netlist_copy)
        netlist_copy.remove(connection)

        # coordinates of chip_a and chip_b
        chip_a = connection[0]
        chip_b = connection[1]
        
        # chip coordinates split into x-, y-, z- coordinates
        x_a = netlist.print.chips[chip_a][0]
        y_a = netlist.print.chips[chip_a][1]
        z_a = netlist.print.chips[chip_a][2]

        x_b = netlist.print.chips[chip_b][0]
        y_b = netlist.print.chips[chip_b][1]
        z_b = netlist.print.chips[chip_b][2]


        origin = (x_a, y_a, z_a)
        current_coordinate = origin
        destination = (x_b, y_b, z_b)

        passed_coordinates = []
        priorities = []
        paths = {}

        while x_a != x_b or y_a != y_b or z_a != z_b:
            current_coordinate = (x_a, y_a, z_a)

            # iterate over all possible directions
            for direction in directions:
                
                temp_x_a = x_a + direction[0]
                temp_y_a = y_a + direction[1]
                temp_z_a = z_a + direction[2]

                temp_coordinate = (temp_x_a, temp_y_a, temp_z_a)

                # assign cost to coordinate based on manhattan distance to destination
                cost = abs(x_b - temp_x_a) + abs(y_b - temp_y_a) + abs(z_b - temp_z_a)
                
                # verify that temporary coordinates are valid coordinates
                if ((not netlist.check_if_path(temp_coordinate) or netlist.check_if_chip(temp_coordinate))
                     and not temp_coordinate in passed_coordinates and not (temp_coordinate, cost) in priorities
                     and ((netlist.check_if_chip(temp_coordinate) and temp_coordinate == destination) or not netlist.check_if_chip(temp_coordinate))
                     and (not temp_x_a < netlist.print.boundaries[0][0] and not temp_x_a > netlist.print.boundaries[1][0] 
                          and not temp_y_a < netlist.print.boundaries[0][1] and not temp_y_a > netlist.print.boundaries[1][1]
                          and not temp_z_a < netlist.print.boundaries[0][2] and not temp_z_a > netlist.print.boundaries[1][2])):
                    
                    # relate new coordinate to old coordinate for tracing
                    paths[temp_coordinate] = current_coordinate

                    # assign cost penalty if coordinate is close to a wrong chip

                    if netlist.check_if_chip((temp_coordinate[0], temp_coordinate[1], temp_coordinate[2] - 1)):
                        cost += 10
                    if netlist.penalty(temp_coordinate, destination):
                        # print(True)
                        cost += 1

                    priorities.append((temp_coordinate, cost))

            # sort valid coordinates on lowest cost to destination
            priorities.sort(key=lambda coordinate: coordinate[1])
           
            # save coordinate as passed coordinate
            passed_coordinates.append(current_coordinate)

            # set new x-, y-, z- coordinates
            try:
                x_a = priorities[0][0][0]
                y_a = priorities[0][0][1]
                z_a = priorities.pop(0)[0][2]
            except IndexError:
                # print(connection)
                return False
        
        # trace route from destination to origin
        netlist.path[connection] = trace(paths, (x_a, y_a, z_a))
        
        # convert path coordinates to x-, y-, z- coordinate lists for visualization via matplotlib
        netlist.path_plot[connection]  = matlib_convert(netlist.path[connection])           
    
    return True