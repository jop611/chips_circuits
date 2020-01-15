"""
A*-algorithm for pathfinding between coordinates
"""

from code.classes.netlist import *
from code.classes.print import *
from code.algorithms.constraints import *
from code.algorithms.helpers import *


def a_star(netlist):
    """ """
    # hardcoded list of all possible directions (north, east, south, west, up, down)
    directions = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    i = 0

    # iterate over all connections in netlist
    for connection in netlist.netlist:


        # dictionary for paths for all connections
        netlist.path[connection] = []

        # coordinates of chip_a and chip_b
        chip_a = connection[0]
        chip_b = connection[1]

        # coordinates split into x- and y-coordinates
        x_a = netlist.print.chips[chip_a][0]
        y_a = netlist.print.chips[chip_a][1]
        z_a = netlist.print.chips[chip_a][2]

        x_b = netlist.print.chips[chip_b][0]
        y_b = netlist.print.chips[chip_b][1]
        z_b = netlist.print.chips[chip_b][2]

        origin = (x_a, y_a, z_a)
        destination = (x_b, y_b, z_b)
        netlist.path[connection] = [(x_a, y_a, z_a)]
        x_path = [x_a]
        y_path = [y_a]
        z_path = [z_a]
        manhattan_distance = x_b - x_a + y_b - y_a

        passed_coordinates = []
        priorities = []
        paths = {}

        while x_a != x_b or y_a != y_b or z_a != z_b:

            # find direction that results in shortest manhattan distance to destination coordinates
            for direction in directions:
                temp_x_a = x_a + direction[0]
                temp_y_a = y_a + direction[1]
                temp_z_a = z_a + direction[2]

                temp_coordinate = (temp_x_a, temp_y_a, temp_z_a)
                distance = abs(x_b - temp_x_a) + abs(y_b - temp_y_a) + abs(z_b - temp_z_a)
                previous_coordinate = (x_a, y_a, z_a)
                # print(direction)
                if not netlist.check_if_path(temp_coordinate) or netlist.check_if_chip(temp_coordinate):
                    # print("Test 1")
                    if not temp_coordinate in passed_coordinates:
                        # print("Test 2")
                        if ((netlist.check_if_chip(temp_coordinate) and temp_coordinate == destination) or not netlist.check_if_chip(temp_coordinate)):
                            # print("Test 3")
                            if (not temp_x_a < netlist.print.boundaries[0][0] and not temp_x_a > netlist.print.boundaries[1][0]
                                and not temp_y_a < netlist.print.boundaries[0][1] and not temp_y_a > netlist.print.boundaries[1][1]
                                and not temp_z_a < netlist.print.boundaries[0][2] and not temp_z_a > netlist.print.boundaries[1][2]):
                                # print("Test 4")
                                if not (temp_coordinate, distance) in priorities:
                                    # print("Test 5")
                                    # previous_coordinate = (x_a, y_a)
                                    paths[temp_coordinate] = previous_coordinate
                                    if netlist.check_if_chip((temp_coordinate[0], temp_coordinate[1], temp_coordinate[2] - 1)):
                                        distance += 10
                                    priorities.append((temp_coordinate, distance))



            # sort list on distance to destination
            priorities.sort(key=lambda coordinate: coordinate[1])

            passed_coordinates.append(previous_coordinate)
            try:
                x_a = priorities[0][0][0]
                y_a = priorities[0][0][1]
                z_a = priorities.pop(0)[0][2]

            except IndexError:
                print(connection)
                return "Failed"



        netlist.path[connection] = trace(paths, (x_a, y_a, z_a))

        print(connection)
        print()
        print (netlist.path[connection])
        print()
        x_y_z_list_tuple  = matlib_convert(netlist.path[connection])
        netlist.path_plot[connection] = x_y_z_list_tuple


        print("Success!!")
        print(f"____\n")
        print()





    return "End of test"
