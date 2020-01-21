from code.classes.netlist import *
from code.classes.print import *
from code.algorithms.helpers import * 


def a_star(netlist):
    """
    A*-algorithm for pathfinding between coordinates
    """

    # hardcoded list of all possible directions (north, east, south, west, up, down)
    directions = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    i = 0
    # netlist.netlist = [(4, 16, 20), (20, 6, 9), (16, 6, 16), (4, 6, 4), (6, 8, 1), (8, 14, 5), (4, 5, 13), 
    # (4, 24, 24), (23, 14, 7), (16, 9, 10), (11, 8, 10), (8, 10, 13), (4, 1, 14), (10, 14, 14), (16, 22, 2), 
    # (11, 5, 4), (16, 18, 7), (21, 11, 7), (24, 5, 11), (21, 20, 15), (14, 19, 3), (23, 17, 5), (23, 12, 7), 
    # (17, 10, 8), (20, 3, 12), (24, 9, 14), (3, 21, 17), (2, 1, 5), (12, 25, 7), (7, 15, 7)]
    # iterate over all connections in netlist
    for connection in netlist.netlist:        
        
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
        blocked_coordinate = (0, 0, 0)
        # blocking_paths = []

        while x_a != x_b or y_a != y_b or z_a != z_b:
            current_coordinate = (x_a, y_a, z_a)

            # iterate over all possible directions
            for direction in directions:
                cost = 0
                temp_x_a = x_a + direction[0]
                temp_y_a = y_a + direction[1]
                temp_z_a = z_a + direction[2]

                temp_coordinate = (temp_x_a, temp_y_a, temp_z_a)

                # assign cost to coordinate based on manhattan distance to destination
                cost = abs(x_b - temp_x_a) + abs(y_b - temp_y_a) + abs(z_b - temp_z_a)
                
                
                # print(netlist.check_if_path(temp_coordinate))
                
                # verify that temporary coordinates are valid coordinates
                if ((not netlist.check_if_path(temp_coordinate) or netlist.check_if_chip(temp_coordinate))
                     and not temp_coordinate in passed_coordinates and not (temp_coordinate, cost) in priorities
                     and ((netlist.check_if_chip(temp_coordinate) and temp_coordinate == destination) or not netlist.check_if_chip(temp_coordinate))
                     and (not temp_x_a < min_x and not temp_x_a > max_x 
                          and not temp_y_a < min_y and not temp_y_a > max_y
                          and not temp_z_a < min_z and not temp_z_a > max_z)):
                    # print(temp_coordinate, cost)
                    # relate new coordinate to old coordinate for tracing
                    paths[temp_coordinate] = current_coordinate

                    # assign cost penalty if coordinate is close to a wrong chip
                    # if netlist.check_if_chip((temp_coordinate[0], temp_coordinate[1], temp_coordinate[2] - 1)):
                    #     cost += 3
                    if netlist.penalty(temp_coordinate, origin, destination):
                        cost += 1

                    # if temp_z_a == 1:

                    #     print(temp_z_a, z_a)
                    #     cost -= 1

                    # if temp_z_a == 2:
                    #     cost -= 2
                    
                    # if temp_z_a == 3:
                    #     cost -= 3



                  

                    if direction == (0, 0, 1):
                        cost -= 2

                    
                    cost -= (temp_z_a + 1)
                    passed_coordinates.append(temp_coordinate)
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

                netlist.clear()
              
                # print("______")
             
                current_index = netlist.netlist.index(connection)
                # netlist.successful_connections = current_index
                

                if current_index != netlist.previous_index:
                    
                    netlist.netlist.insert(netlist.netlist.index(connection) - 1, netlist.netlist.pop(netlist.netlist.index(connection)))
                    # netlist.previous_connection = connection
                    
                    
                
                else:
                    netlist.netlist.insert(0, netlist.netlist.pop(netlist.netlist.index(netlist.previous_connection)))
                    netlist.netlist.insert(1, netlist.netlist.pop(netlist.netlist.index(connection)))
                    # print(netlist.netlist.index(netlist.previous_connection))
                    # netlist.netlist.insert(netlist.netlist.index(netlist.previous_connection) - 1, netlist.netlist.pop(netlist.netlist.index(netlist.previous_connection)))
                    # netlist.netlist.insert(netlist.netlist.index(connection) - 1, netlist.netlist.pop(netlist.netlist.index(connection))) 
                   

               
                netlist.previous_connection = connection
                # netlist.previous_connection = connection
                netlist.previous_index = current_index
                
                # print("______")
                # print(netlist.netlist)
                # print("______")

                #     return False
                return False
                
        # trace route from destination to origin
        netlist.path[connection] = trace(paths, (x_a, y_a, z_a))
        
        # convert path coordinates to x-, y-, z- coordinate lists for visualization via matplotlib
        netlist.path_plot[connection]  = matlib_convert(netlist.path[connection])           
    # print("lol")
    print(netlist.test())
    print(netlist.path)
    netlist.score()
    netlist.save_result()
    return True
