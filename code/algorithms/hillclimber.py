"""
hillclimber.py

Recreate connections made with A* algoritme with Hillclimber algorithm

(C) 2020 Teamname, Amsterdam, The Netherlands
"""

from code.classes.netlist import *
from code.classes.print import *
from code.algorithms.helpers import *
from random import shuffle

def hillclimber(netlist):
    """Hillclimber algorithm for pathfinding between coordinate"""

    import_result(netlist, netlist.print_nr, netlist.netlist_nr)
    current_length = netlist.length

    # hardcoded list of all possible directions (north, east, south, west, up, down)
    directions = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]

    # ...
    while True:
        current_length = netlist.length
        netlist.netlist.sort(key=lambda connection: len(netlist.path[connection]))
        
        # iterate over all connections in netlist
        for connection in netlist.netlist:
            del netlist.path[connection]

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
            blocking_paths = []

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

                    # print(netlist.check_if_path(temp_coordinate))

                    # verify that temporary coordinates are valid coordinates
                    if ((not netlist.check_if_path(temp_coordinate) or netlist.check_if_chip(temp_coordinate))
                        and not temp_coordinate in paths and not (temp_coordinate, cost) in priorities
                        and ((netlist.check_if_chip(temp_coordinate) and temp_coordinate == destination) or not netlist.check_if_chip(temp_coordinate))
                        and (not temp_x_a < netlist.print.boundaries[0][0] and not temp_x_a > netlist.print.boundaries[1][0]
                            and not temp_y_a < netlist.print.boundaries[0][1] and not temp_y_a > netlist.print.boundaries[1][1]
                            and not temp_z_a < netlist.print.boundaries[0][2] and not temp_z_a > netlist.print.boundaries[1][2])):

                        # relate new coordinate to old coordinate for tracing
                        paths[temp_coordinate] = current_coordinate

                        if netlist.penalty(temp_coordinate, origin, destination):
                            cost += 1

                        priorities.append((temp_coordinate, cost))

                # sort valid coordinates on lowest cost to destination
                priorities.sort(key=lambda coordinate: coordinate[1])

                # save coordinate as passed coordinate
                x_a = priorities[0][0][0]
                y_a = priorities[0][0][1]
                z_a = priorities.pop(0)[0][2]

            # trace route from destination to origin
            netlist.path[connection] = trace(paths, (x_a, y_a, z_a))

            # convert path coordinates to x-, y-, z- coordinate lists for visualization via matplotlib
            netlist.path_plot[connection]  = matlib_convert(netlist.path[connection])

        # count amount of wires used
        netlist.score()

        #
        if netlist.length == current_length:
            netlist.save_result()
            break

def import_result(netlist, print_nr, netlist_nr):
    """Open A* solution file needed to be shortened"""

    length = input("Lengte van oplossing om te hillclimben: ")
    with open(f'results/print_{print_nr}/a_star/netlist_{netlist_nr}_{length}.txt', newline='') as infile:
        data = json.load(infile)

        # ..
        for connection in data["paths"]:
            key = (connection[0][0], connection[0][1], connection[0][2])
            netlist.path[key] = []

            # ..
            for coordinate in connection[1]:
                coordinate_tuple = (coordinate[0], coordinate[1], coordinate[2])
                netlist.path[key].append(coordinate_tuple)
