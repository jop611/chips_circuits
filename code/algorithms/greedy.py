from code.classes.netlist import *
from code.algorithms.random import *
from code.classes.print import *

def greedy(netlist, connection):
    # temporary 
    if not netlist.path:
        netlist.path = []
    chip_a = connection[0]
    chip_b = connection[1]
    max_x_boundary = netlist.print.boundaries[1][0]
    max_y_boundary = netlist.print.boundaries[1][1]

    x_a = netlist.print.chips[chip_a][0]
    y_a = netlist.print.chips[chip_a][1]
    x_b = netlist.print.chips[chip_b][0]
    y_b = netlist.print.chips[chip_b][1]

    path_x = [x_a]
    path_y = [y_a]

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
        directions = [(x_a-1, y_a), (x_a+1, y_a), (x_a, y_a-1), (x_a, y_a+1)]
        possible_directions = []
        if diff_x < 0:
            new_direction = directions[0]
            if not new_direction in netlist.path and (0 <= new_direction[0] <= max_x_boundary):
                x_a = new_direction[0]
                diff_x = x_b - x_a
            else:
                for direction in directions:
                    if direction in netlist.path or direction[0] > max_x_boundary or direction[1] > max_y_boundary or direction[0] < 0 or direction[1] < 0:
                        print("oh oh")
                        pass
                    else:
                        possible_directions.append(direction)
                if len(possible_directions) != 0:
                    random_direction = Random(possible_directions)
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
            if not new_direction in netlist.path and (0 <= new_direction[0] <= max_x_boundary):
                x_a = new_direction[0]
                diff_x = x_b - x_a
            else:
                for direction in directions:
                    if direction in netlist.path or direction[0] > max_x_boundary or direction[1] > max_y_boundary or direction[0] < 0 or direction[1] < 0:
                        print("oh oh")
                        pass
                    else:
                        possible_directions.append(direction)
                if len(possible_directions) != 0:
                    random_direction = Random(possible_directions)
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
            if not new_direction in netlist.path and (0 <= new_direction[1] <= max_y_boundary):
                y_a = new_direction[1]
                print(f"y_a: {y_a}")
                print(new_direction)
                diff_y = y_b - y_a
                print(f"new dif_y: {diff_y}")
            else:
                for direction in directions:
                    if direction in netlist.path or direction[0] > max_x_boundary or direction[1] > max_y_boundary or direction[0] < 0 or direction[1] < 0:
                        print("oh oh")
                        pass
                    else:
                        possible_directions.append(direction)
                if len(possible_directions) != 0:
                    random_direction = Random(possible_directions)
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
            if not new_direction in netlist.path and (0 <= new_direction[1] <= max_y_boundary):
                y_a = new_direction[1]
                diff_y = y_b - y_a
            else:
                for direction in directions:
                    if direction in netlist.path or direction[0] > max_x_boundary or direction[1] > max_y_boundary or direction[0] < 0 or direction[1] < 0:
                        print("oh oh")
                        pass
                    else:
                        possible_directions.append(direction)
                if len(possible_directions) != 0:
                    random_direction = Random(possible_directions)
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
        netlist.path_plot[connection] = (path_x, path_y)
        netlist.path.append((x_a, y_a))
    print(netlist.path)
    print((2, 3) in netlist.path)