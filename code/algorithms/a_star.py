from code.classes.netlist import *
from code.classes.print import *
from code.algorithms.constraints import *
from code.algorithms.helpers import * 


def a_star(netlist):
    """
    A*-algorithm for pathfinding between coordinates
    """

    # hardcoded list of all possible directions
    directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

    # iterate over all connections in netlist
    # connection = netlist.netlist[3]
    for connection in netlist.netlist:
        print()
        print(connection)
        print()
        # dictionary for paths for all connections
        netlist.path[connection] = []

        # coordinates of chip_a and chip_b
        chip_a = connection[0]
        chip_b = connection[1]
        
        # coordinates split into x- and y-coordinates
        x_a = netlist.print.chips[chip_a][0]
        y_a = netlist.print.chips[chip_a][1]
        x_b = netlist.print.chips[chip_b][0]
        y_b = netlist.print.chips[chip_b][1] 

        netlist.path[connection] = [(x_a, y_a)]
        x_path = [x_a]
        y_path = [y_a]
        manhattan_distance = x_b - x_a + y_b - y_a

        
        priorities = []
        paths = {}
        while x_a != x_b or y_a != y_b:
        
            # find direction that results in shortest manhattan distance to destination coordinates
            for direction in directions: 
                temp_x_a = x_a + direction[0]
                temp_y_a = y_a + direction[1]
                distance = abs(x_b - temp_x_a) + abs(y_b - temp_y_a)

                # append adjacent coordinates and distance to destination to list
                priorities.append((temp_x_a, temp_y_a, distance))

            # sort list on distance to destination
            priorities.sort(key=lambda coordinate: coordinate[2])
            # print(priorities)
    
            # for priority in priorities:
            #     for direction in directions:
            #         x_a = priority[0]
            #         y_a = priority[1]

            #         temp_x_a = x_a + direction[0]
            #         temp_y_a += x_a + direction[1]
            previous_coordinate = (x_a, y_a)
            x_a = priorities[0][0]
            y_a = priorities.pop(0)[1]
            
            paths[(x_a, y_a)] = previous_coordinate
            

            x_path.append(x_a)
            y_path.append(y_a)
            netlist.path[connection].append((x_a, y_a))
            netlist.path_plot[connection] = (x_path, y_path)
            netlist.length += 1
            
        # print(netlist.path[connection])
        netlist.path[connection] = trace(paths, (x_a, y_a))
        print(netlist.path[connection])           
    
    return "End of test"
