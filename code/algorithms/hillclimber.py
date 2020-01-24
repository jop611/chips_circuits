from code.classes.netlist import *
from code.classes.print import *
from code.algorithms.helpers import * 


def hillclimber(netlist):
    """
    A*-algorithm for pathfinding between coordinates
    """

    import_result(netlist, netlist.print_nr, netlist.netlist_nr)
    current_length = netlist.length
    
    # hardcoded list of all possible directions (north, east, south, west, up, down)
    directions = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]
    i = 0
    # netlist.netlist = [(11, 8, 10), (8, 10, 13), (8, 14, 5), (11, 5, 4), (16, 6, 16), 
    #                    (16, 9, 10), (16, 22, 2), (24, 5, 11), (14, 19, 3), (4, 6, 4), 
    #                    (17, 10, 8), (10, 14, 14), (20, 6, 9), (4, 16, 20), (16, 18, 7), 
    #                    (3, 21, 17), (21, 11, 7), (23, 14, 7), (6, 8, 1), (4, 5, 13), 
    #                    (4, 24, 24), (4, 1, 14), (21, 20, 15), (23, 17, 5), (23, 12, 7), 
    #                    (20, 3, 12), (24, 9, 14), (2, 1, 5), (12, 25, 7), (7, 15, 7)]
    # iterate over all connections in netlist
    while True:
        current_length = netlist.length
        netlist.netlist.sort(key=lambda connection: len(netlist.path[connection]), reverse=True)
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

                        # assign cost penalty if coordinate is close to a wrong chip
                        # if netlist.check_if_chip((temp_coordinate[0], temp_coordinate[1], temp_coordinate[2] - 1)):
                        #     cost += 3
                        # if netlist.penalty(temp_coordinate, origin, destination):
                        #     cost += 1

                        priorities.append((temp_coordinate, cost))


                    # sort valid coordinates on lowest cost to destination
                priorities.sort(key=lambda coordinate: coordinate[1])
                
                    # save coordinate as passed coordinate
                
                # try:
                        # set new x-, y-, z- coordinates
                        # try:
                x_a = priorities[0][0][0]
                y_a = priorities[0][0][1]
                z_a = priorities.pop(0)[0][2]

                # except IndexError:
                    
                #     # except IndexError:
                #     #     # print("______")
                #     #     # print(connection)
                #     #     # print(netlist.netlist)
                #     #     # print()
                #     #     try:
                #     #         netlist.dick[connection] += 1
                #     #     except KeyError:
                #     #         netlist.dick[connection] = 1
                #     netlist.clear()
                #         # netlist.netlist.insert(netlist.netlist.index(connection) - 1, netlist.netlist.pop(netlist.netlist.index(connection)))
                #     netlist.netlist.insert(0, netlist.netlist.pop(netlist.netlist.index(connection)))


                #     #     # netlist.netlist.remove(connection)
                #     #     # print(netlist.netlist)
                #     #     # print("______")

                #     #     return False
                #     return False

            # trace route from destination to origin
            netlist.path[connection] = trace(paths, (x_a, y_a, z_a))
            
            # convert path coordinates to x-, y-, z- coordinate lists for visualization via matplotlib
            netlist.path_plot[connection]  = matlib_convert(netlist.path[connection])           
        
        netlist.test()

        netlist.score()
        netlist.save_result()
        if netlist.length == current_length:
            break
        # return False


def import_result(netlist, print_nr, netlist_nr):
    with open(f'results/print_{print_nr}/netlist_{netlist_nr}_1.txt', newline='') as infile:
        data = json.load(infile)
        # print(data)
        for connection in data["paths"]:
            key = (connection[0][0], connection[0][1], connection[0][2])
            netlist.path[key] = []
            for coordinate in connection[1]:
                coordinate_tuple = (coordinate[0], coordinate[1], coordinate[2]) 
                netlist.path[key].append(coordinate_tuple)
        
    # print(netlist.path)


            
            # keep track of amount of occurences of gate in netlist
            # try:
            #     self.connections_count[int(chip_a)] += 1
            # except KeyError:
            #     self.connections_count[int(chip_a)] = 1
            # except ValueError:
            #     pass

            # try:
            #     self.connections_count[int(chip_b)] += 1
            # except KeyError:
            #     self.connections_count[int(chip_b)] = 1
            # except ValueError:
            #     pass

            # try:
            #     manhattan_distance = abs(self.print.chips[int(chip_b)][0] - self.print.chips[int(chip_a)][0]) + abs(self.print.chips[int(chip_b)][1] - self.print.chips[int(chip_a)][1])
            #     netlist.append((int(chip_a), int(chip_b), manhattan_distance))        
            #     self.lowerbound += manhattan_distance
            #     self.chip_occurences.append(int(chip_a))
            #     self.chip_occurences.append(int(chip_b))
            # except ValueError:
            #     pass
        # print(self.path)