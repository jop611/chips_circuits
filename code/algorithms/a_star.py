"""
a_star.py

A*-algorithm for pathfinding between coordinates for given netlist.
Returns Boolean function.

(C) 2020 Teamname, Amsterdam, The Netherlands
"""

from code.classes.netlist import Netlist
from code.algorithms.helpers import *

def a_star(netlist):
    """
    A*-algorithm for pathfinding between coordinates
    """

    # hardcoded list of all possible directions (north, east, south, west, up, down)
    directions = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    
    # iterate over all connections in netlist
    for connection in netlist.netlist:

        # coordinates of gate_a and gate_b
        gate_a = connection[0]
        gate_b = connection[1]

        # gate coordinates split into x-, y-, z- coordinates
        x_a = netlist.print.gates[gate_a][0]
        y_a = netlist.print.gates[gate_a][1]
        z_a = netlist.print.gates[gate_a][2]

        x_b = netlist.print.gates[gate_b][0]
        y_b = netlist.print.gates[gate_b][1]
        z_b = netlist.print.gates[gate_b][2]

        # setting the boundaries of the grid
        min_x = netlist.print.boundaries[0][0]
        max_x = netlist.print.boundaries[1][0]
        min_y = netlist.print.boundaries[0][1]
        max_y = netlist.print.boundaries[1][1]
        min_z = netlist.print.boundaries[0][2]
        max_z = netlist.print.boundaries[1][2]

        # defining the origin & destination coordinates
        origin = (x_a, y_a, z_a)
        current_coordinate = origin
        destination = (x_b, y_b, z_b)

        priorities = []
        paths = {}

        # perform pathfinding until the destination coordinate is reached
        while x_a != x_b or y_a != y_b or z_a != z_b:
            current_coordinate = (x_a, y_a, z_a)

            # iterate over all possible directions
            for direction in directions:

                # create temporary coordinates
                temp_x_a = x_a + direction[0]
                temp_y_a = y_a + direction[1]
                temp_z_a = z_a + direction[2]

                # coordinate of a possible direction
                temp_coordinate = (temp_x_a, temp_y_a, temp_z_a)

                # calculate manhattan distance to destination
                cost = abs(x_b - temp_x_a) + abs(y_b - temp_y_a) + abs(z_b - temp_z_a)

                # verify that temporary coordinates are valid coordinates
                if ((not netlist.check_if_path(temp_coordinate) or netlist.check_if_gate(temp_coordinate))
                     and not temp_coordinate in paths and not (temp_coordinate, cost) in priorities
                     and ((netlist.check_if_gate(temp_coordinate) and temp_coordinate == destination) or not netlist.check_if_gate(temp_coordinate))
                     and (not temp_x_a < min_x and not temp_x_a > max_x
                          and not temp_y_a < min_y and not temp_y_a > max_y
                          and not temp_z_a < min_z and not temp_z_a > max_z)):

                    # relate new coordinate to old coordinate for tracing
                    paths[temp_coordinate] = current_coordinate

                    # increasing cost if coordinate is close to a wrong gate so that it avoids it
                    if netlist.penalty(temp_coordinate, origin, destination):
                        cost += 1

                    # reducing cost if an upward movement is possible so that it is forced upwards
                    if direction == (0, 0, 1):
                        cost -= 2
                    cost -= temp_z_a * 2

                    # add temporary to list of valid coordinates
                    priorities.append((temp_coordinate, cost))

            # sort valid coordinates on lowest cost to destination
            priorities.sort(key=lambda coordinate: coordinate[1])

            # set new x-, y-, z- coordinates if there are valid coordinates to go to
            if len(priorities) != 0:
                x_a = priorities[0][0][0]
                y_a = priorities[0][0][1]
                z_a = priorities.pop(0)[0][2]

            # remove all succesful paths, move failed connection to front of netlist
            else:
                netlist.clear()
                netlist.netlist.insert(0, netlist.netlist.pop(netlist.netlist.index(connection)))
                return False

        # trace route from destination to origin
        netlist.path[connection] = trace(paths, (x_a, y_a, z_a))

        # convert path coordinates to x-, y-, z- coordinate lists for visualization via matplotlib
        netlist.path_plot[connection]  = matlib_convert(netlist.path[connection])

    # count amount of wires used
    netlist.score()

    # save solution in json format
    netlist.save_result()
    return True

