from code.classes.netlist import *
from code.classes.print import *
from code.algorithms.helpers import * 
import random


def a_star(netlist):
    """
    A*-algorithm for pathfinding between coordinates
    """

    # hardcoded list of all possible directions (north, east, south, west, up, down)
    directions = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    i = 0
    
    # randomly sorting the netlist
    random.shuffle(netlist.netlist)
    
    for connection in netlist.netlist:        
        
        # coordinates of chip_a and chip_b
        chip_a = connection[0]
        chip_b = connection[1]
        manhattan_distance = connection[2]
        
        # chip coordinates split into x-, y-, z- coordinates
        x_a = netlist.print.chips[chip_a][0]
        y_a = netlist.print.chips[chip_a][1]
        z_a = netlist.print.chips[chip_a][2]

        x_b = netlist.print.chips[chip_b][0]
        y_b = netlist.print.chips[chip_b][1]
        z_b = netlist.print.chips[chip_b][2]

        diff_x = x_b - x_a
        diff_y = y_b - y_a
        diff_diff = diff_x - diff_y

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
        blocked = {}
        blocked_coordinate = (0, 0, 0)
        blocked[connection] = False

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
                     and not temp_coordinate in paths and not (temp_coordinate, cost) in priorities
                     and ((netlist.check_if_chip(temp_coordinate) and temp_coordinate == destination) or not netlist.check_if_chip(temp_coordinate))
                     and (not temp_x_a < min_x and not temp_x_a > max_x 
                          and not temp_y_a < min_y and not temp_y_a > max_y
                          and not temp_z_a < min_z and not temp_z_a > max_z)):
                    
                    # relate new coordinate to old coordinate for tracing
                    paths[temp_coordinate] = current_coordinate

                    # assign cost if neighbouring                     
                    if netlist.penalty(temp_coordinate, origin, destination):
                        cost += 1

                    # if direction == (0, 0, 1):
                    #     cost -= 2
                    # if manhattan_distance < 10 and temp_z_a <= 3:
                    #     cost -= (temp_z_a * 4)
                    # elif manhattan_distance < 10:
                    #     cost -= (temp_z_a * 2)
                    # elif manhattan_distance > 10 and temp_z_a > 3:
                    #     cost -= (temp_z_a * 4)
                    # elif manhattan_distance > 10:
                    #     cost -= (temp_z_a * 2)

                    # if blocked[connection] != True:
                    if direction == (0, 0, 1):
                        cost -= 2
                    #     if manhattan_distance < 10 and temp_z_a <= 3:
                    #         cost -= (temp_z_a * 3)
                    #     elif manhattan_distance < 10:
                    #         cost -= (temp_z_a * 1)
                    #     elif manhattan_distance > 10 and temp_z_a > 3:
                    #         cost -= (temp_z_a * 3)
                    #     elif manhattan_distance > 10:
                    #         cost -= (temp_z_a * 1)
                    cost -= (temp_z_a * 2)
                        
                    # if temp_x_a == 0 or temp_y_a == 0:
                    #     cost -= 1




                        



                    
                    # cost -= (temp_z_a * 2)
                    # passed_coordinates.append(temp_coordinate)
                    priorities.append((temp_coordinate, cost))
                   
                # elif netlist.check_if_path(temp_coordinate) and not netlist.check_if_chip(temp_coordinate) and len(priorities) == 0 and direction != (0, 0, 1) and direction != (0, 0, -1):
                    
                #     blocked_coordinate = temp_coordinate
                #     print(blocked_coordinate)

                # sort valid coordinates on lowest cost to destination
            priorities.sort(key=lambda coordinate: coordinate[1])
            
                # save coordinate as passed coordinate
           


            try:
                    # set new x-, y-, z- coordinates
                    # try:
                x_a = priorities[0][0][0]
                y_a = priorities[0][0][1]
                z_a = priorities.pop(0)[0][2]

            except IndexError:

                # netlist.clear()
                # print("______")
                # print(netlist.netlist)   
                # netlist.netlist.insert(0, netlist.netlist.pop(netlist.netlist.index(connection)))
                netlist.clear()
                #     return False
                return False
                
        # trace route from destination to origin
        netlist.path[connection] = trace(paths, (x_a, y_a, z_a))
        
        # convert path coordinates to x-, y-, z- coordinate lists for visualization via matplotlib
        netlist.path_plot[connection]  = matlib_convert(netlist.path[connection])          
    # print("lol")
    if netlist.test() == False:
        return False
    # print(netlist.path)
    netlist.score()
    netlist.save_result()
    return True
