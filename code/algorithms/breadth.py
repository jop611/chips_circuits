"""
Breadth.py

Breadth First algorithm for pathfinding between coordinates for given netlist.
Returns Boolean function, True if all connections are made and False if not all connections could be made

(C) 2020 Teamname, Amsterdam, The Netherlands
"""

import queue
from code.classes.netlist import *
from code.classes.print import *
from code.algorithms.helpers import *


def bfs(netlist):
    """Breadth First algorithm for pathfinding between coordinates"""

    directions = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
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

        origin = (x_a, y_a, z_a)
        current_coordinate = origin
        destination = (x_b, y_b, z_b)

        passed_coordinates = []
        priorities = []
        paths = {}

        while x_a != x_b or y_a != y_b or z_a != z_b:

            current_coordinate = (x_a, y_a, z_a)
            coordinates_to_sort = []

            # iterate over all possible directions
            for direction in directions:

                # create temporary coordinates for validation of moves
                temp_x_a = x_a + direction[0]
                temp_y_a = y_a + direction[1]
                temp_z_a = z_a + direction[2]

                temp_coordinate = (temp_x_a, temp_y_a, temp_z_a)

                # verify that temporary coordinates are valid coordinates
                if ((not netlist.check_if_path(temp_coordinate) or netlist.check_if_gate(temp_coordinate))
                     and not temp_coordinate in paths and not temp_coordinate in priorities
                     and ((netlist.check_if_gate(temp_coordinate) and temp_coordinate == destination) or not netlist.check_if_gate(temp_coordinate))
                     and (not temp_x_a < netlist.print.boundaries[0][0] and not temp_x_a > netlist.print.boundaries[1][0]
                          and not temp_y_a < netlist.print.boundaries[0][1] and not temp_y_a > netlist.print.boundaries[1][1]
                          and not temp_z_a < netlist.print.boundaries[0][2] and not temp_z_a > netlist.print.boundaries[1][2])):

                    # relate new coordinate to old coordinate for future tracing
                    paths[temp_coordinate] = current_coordinate

                    priorities.append(temp_coordinate)

            # set new x-, y-, z- coordinates
            if len(priorities) != 0:
                x_a = priorities[0][0]
                y_a = priorities[0][1]
                z_a = priorities.pop(0)[2]

            # clear successful paths, move failed connection to front of netlist
            else:
                netlist.clear()
                netlist.netlist.insert(0, netlist.netlist.pop(netlist.netlist.index(connection)))
                return False

        # trace route from destination to origin
        netlist.path[connection] = trace(paths, (x_a, y_a, z_a))

        # convert path coordinates to x-, y-, z- coordinate lists for visualization via matplotlib
        netlist.path_plot[connection]  = matlib_convert(netlist.path[connection])

    netlist.score()
    netlist.save_result()
    return True
