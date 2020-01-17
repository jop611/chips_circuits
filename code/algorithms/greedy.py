from code.classes.netlist import *
from code.algorithms.random import *
from code.classes.print import *

def greedy(netlist):

    for connection in netlist.netlist:

        # temporary 

        netlist.path[connection] = []

        chip_a = connection[0]
        chip_b = connection[1]
        max_x_boundary = netlist.print.boundaries[1][0]
        max_y_boundary = netlist.print.boundaries[1][1]

        x_a = netlist.print.chips[chip_a][0]
        y_a = netlist.print.chips[chip_a][1]
        z_a = netlist.print.chips[chip_a][2]
        x_b = netlist.print.chips[chip_b][0]
        y_b = netlist.print.chips[chip_b][1]
        z_b = netlist.print.chips[chip_b][2]
        
        origin = (x_a, y_a, z_a)
        destination = (x_b, y_b, z_b)

        path_x = [x_a]
        path_y = [y_a]
        path_z = [z_a]

        diff_x = x_b - x_a
        diff_y = y_b - y_a
        # directions = [(x_a-1, y_a), (x_a+1, y_a), (x_a, y_a-1), (x_a, y_a+1)]
        

        print(connection)
        print(f"diff_x: {diff_x}")
        print(f"diff_y: {diff_y}")
        print(f"start x_a: {x_a}")
        print(f"start y_a: {y_a}")
        print(f"x_b:{x_b}")
        print(f"y_b:{y_b}")
        
        while x_a != x_b or y_a != y_b:

            # directions = adjacent coordinates
            directions = [(x_a-1, y_a, 0), (x_a+1, y_a, 0), (x_a, y_a-1, 0), (x_a, y_a+1, 0)]

            possible_directions = []
            if diff_x < 0:
                new_direction = directions[0]
                if ((not netlist.check_if_path(new_direction) or netlist.check_if_chip(new_direction))
                    #  and not temp_coordinate in passed_coordinates and not (temp_coordinate, cost) in priorities
                     and ((netlist.check_if_chip(new_direction) and new_direction == destination) or not netlist.check_if_chip(new_direction))
                     and (not new_direction[0] < 0 and not new_direction[0] > max_x_boundary and not new_direction[1] < 0 and not new_direction[1] > max_y_boundary)):
                        #   and not temp_z_a < netlist.print.boundaries[0][2] and not temp_z_a > netlist.print.boundaries[1][2])):
                    x_a = new_direction[0]
                    diff_x = x_b - x_a
                else:
                    for direction in directions:
                        if ((not netlist.check_if_path(direction) or netlist.check_if_chip(direction))
                             #  and not temp_coordinate in passed_coordinates and not (temp_coordinate, cost) in priorities
                             and ((netlist.check_if_chip(direction) and direction == destination) or not netlist.check_if_chip(direction))
                             and (not direction[0] < 0 and not direction[0] > max_x_boundary and not direction[1] < 0 and not direction[1] > max_y_boundary)):
          
                            possible_directions.append(direction)
                    if len(possible_directions) != 0:
                        random_direction = randomize(possible_directions)
                        print(possible_directions)
                        print(random_direction)
                        x_a = random_direction[0]
                        y_a = random_direction[1]
                        diff_x = x_b - x_a
                        diff_y = y_b - y_a
                    else:
                        print("No available way")
                        break
            elif diff_x > 0:
                new_direction = directions[1]
                if ((not netlist.check_if_path(new_direction) or netlist.check_if_chip(new_direction))
                    #  and not temp_coordinate in passed_coordinates and not (temp_coordinate, cost) in priorities
                     and ((netlist.check_if_chip(new_direction) and new_direction == destination) or not netlist.check_if_chip(new_direction))
                     and (not direction[0] < 0 and not direction[0] > max_x_boundary and not direction[1] < 0 and not direction[1] > max_y_boundary)):
                    x_a = new_direction[0]
                    diff_x = x_b - x_a
                else:
                    for direction in directions:
                        if ((not netlist.check_if_path(direction) or netlist.check_if_chip(direction))
                             #  and not temp_coordinate in passed_coordinates and not (temp_coordinate, cost) in priorities
                             and ((netlist.check_if_chip(direction) and direction == destination) or not netlist.check_if_chip(direction))
                             and (not direction[0] < 0 and not direction[0] > max_x_boundary and not direction[1] < 0 and not direction[1] > max_y_boundary)):
                   
                            possible_directions.append(direction)

                    if len(possible_directions) != 0:
                        random_direction = randomize(possible_directions)
                        print(possible_directions)
                        print(random_direction)
                        x_a = random_direction[0]
                        y_a = random_direction[1]
                        diff_x = x_b - x_a
                        diff_y = y_b - y_a
                    else:
                        print("No available way")
                        break
            elif diff_y < 0:
                new_direction = directions[2]
                if ((not netlist.check_if_path(new_direction) or netlist.check_if_chip(new_direction))
                    #  and not temp_coordinate in passed_coordinates and not (temp_coordinate, cost) in priorities
                     and ((netlist.check_if_chip(new_direction) and new_direction == destination) or not netlist.check_if_chip(new_direction))
                     and (not direction[0] < 0 and not direction[0] > max_x_boundary and not direction[1] < 0 and not direction[1] > max_y_boundary)):
                    y_a = new_direction[1]
                    print(f"y_a: {y_a}")
                    print(new_direction)
                    diff_y = y_b - y_a
                    print(f"new dif_y: {diff_y}")
                else:
                    for direction in directions:
                        if ((not netlist.check_if_path(direction) or netlist.check_if_chip(direction))
                             #  and not temp_coordinate in passed_coordinates and not (temp_coordinate, cost) in priorities
                             and ((netlist.check_if_chip(direction) and direction == destination) or not netlist.check_if_chip(direction))
                             and (not direction[0] < 0 and not direction[0] > max_x_boundary and not direction[1] < 0 and not direction[1] > max_y_boundary)):
                        
                            possible_directions.append(direction)
                    if len(possible_directions) != 0:
                        random_direction = randomize(possible_directions)
                        print(possible_directions)
                        print(random_direction)
                        x_a = random_direction[0]
                        y_a = random_direction[1]
                        diff_x = x_b - x_a
                        diff_y = y_b - y_a
                    else:
                        print("No available way")
                        break
            elif diff_y > 0:
                new_direction = directions[3]
                if ((not netlist.check_if_path(new_direction) or netlist.check_if_chip(new_direction))
                    #  and not temp_coordinate in passed_coordinates and not (temp_coordinate, cost) in priorities
                     and ((netlist.check_if_chip(new_direction) and new_direction == destination) or not netlist.check_if_chip(new_direction))
                     and (not direction[0] < 0 and not direction[0] > max_x_boundary and not direction[1] < 0 and not direction[1] > max_y_boundary)):
                    y_a = new_direction[1]
                    diff_y = y_b - y_a
                else:
                    for direction in directions:
                        if ((not netlist.check_if_path(direction) or netlist.check_if_chip(direction))
                             #  and not temp_coordinate in passed_coordinates and not (temp_coordinate, cost) in priorities
                             and ((netlist.check_if_chip(direction) and direction == destination) or not netlist.check_if_chip(direction))
                             and (not direction[0] < 0 and not direction[0] > max_x_boundary and not direction[1] < 0 and not direction[1] > max_y_boundary)):

                            possible_directions.append(direction)
                    if len(possible_directions) != 0:
                        random_direction = randomize(possible_directions)
                        print(possible_directions)
                        print(random_direction)
                        x_a = random_direction[0]
                        y_a = random_direction[1]
                        diff_x = x_b - x_a
                        diff_y = y_b - y_a
                    else:
                        print("No available way")
                        break
            print(f"na 1 stap x-waarde: {x_a}")
            print(f"na 1 stap y-waarde: {y_a}")
            
            # netlist.path[connection].append((x_a, y_a))
            path_x.append(x_a)
            path_y.append(y_a)
            path_z.append(0)
            netlist.path_plot[connection] = (path_x, path_y, path_z)
            netlist.path[connection].append((x_a, y_a, z_a))
        print(netlist.path)
        print((2, 3, 0) in netlist.path)