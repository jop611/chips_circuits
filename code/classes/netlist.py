import csv
from code.algorithms.constraints import *

class Netlist():
    def __init__(self, print_nr, netlist_nr):
        self.gates = {}
        self.path = {}
        self.max_x = 0
        self.max_y = 0
        self.x_list = []
        self.y_list = []

        # map x, y coordinates of chips
        self.load_print(print_nr, netlist_nr)
            
        self.boundaries = ((0, 0), (self.max_x + 1, self.max_y + 1))
        print(self.boundaries)
        
        
        self.netlist = self.load_netlist(print_nr, netlist_nr) 
        print(self.netlist)
        print()


    def load_print(self, print_nr, netlist_nr):



        with open(f'gates&netlists/chip_{print_nr}/print_{print_nr}.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for chip, x, y in reader:
                try:
                    self.gates[int(chip)] = (int(x), int(y))
                    self.x_list.append(int(x))
                    self.y_list.append(int(y))

                    # set boundaries of grid
                    if int(x) > self.max_x:
                       self.max_x = int(x)
                    if int(y) > self.max_y:
                        self.max_y = int(y) 
                except ValueError:
                    pass
    
    
    def load_netlist(self, print_nr, netlist_nr):

        netlist = []
        with open(f'gates&netlists/chip_{print_nr}/netlist_{netlist_nr}.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for chip_a, chip_b in reader:
                try:
                    manhattan_distance = abs(self.gates[int(chip_b)][0] - self.gates[int(chip_a)][0]) + abs(self.gates[int(chip_b)][1] - self.gates[int(chip_a)][1])
                    netlist.append((int(chip_a), int(chip_b), manhattan_distance))
                except ValueError:
                    pass
            netlist.sort(key=lambda connection: connection[2])
        return netlist


    def connect(self, connection):
        self.path[connection] = []
        chip_a = connection[0]
        chip_b = connection[1]
        print(connection)
        x_a = self.gates[chip_a][0]
        y_a = self.gates[chip_a][1]
        x_b = self.gates[chip_b][0]
        y_b = self.gates[chip_b][1]

        print(f"chip a: {x_a}, {y_a}\nchip_b: {x_b}, {y_b}")

        diff_x = x_b - x_a
        diff_y = y_b - y_a

        while x_a != x_b or y_a != y_b:
            if diff_x < 0:
                # if not self.check_for_chip((x_a - 1, y_a)):
                x_a -= 1
                diff_x = x_b - x_a 
            elif diff_x > 0:
                # self.check_for_chip((x_a + 1, y_a))
                x_a += 1  
                diff_x = x_b - x_a     
            elif diff_y < 0:
                # self.check_for_chip((x_a, y_a - 1))
                y_a -= 1
                diff_y = y_b - y_a
            elif diff_y > 0:
                # self.check_for_chip((x_a, y_a + 1))
                y_a += 1
                diff_y = y_b - y_a

            self.path[connection].append((x_a, y_a))

        print(self.path[connection])

