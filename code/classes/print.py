"""
print.py

Import locations of gates on a grid.

(C) 2020 Teamname, Amsterdam, The Netherlands
"""

import csv


class Print():

    def __init__(self, print_nr):
        self.max_x = 0
        self.max_y = 0
        self.max_z = 7
        self.x_list = []
        self.y_list = []
        self.z_list = []
        self.gates_locations = []
        self.gates = self.load_print(print_nr)
        self.boundaries = ((0, 0, 0), (self.max_x + 1, self.max_y + 1, 7))
        self.gate_count = len(self.gates)


    def load_print(self, print_nr):
        """
        Load locations of gates in grid from a .csv file.
        
        Input:
        print_nr; string of numeric value.
        
        Return:
        List containing of tuples of x-, y-, z-coordinates.
        """

        gates = {}

        # open .csv file
        with open(f'gates&netlists/chip_{print_nr}/print_{print_nr}.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for gate, x, y in reader:
                try:
                    gates[int(gate)] = (int(x), int(y), 0)
                    self.x_list.append(int(x))
                    self.y_list.append(int(y))
                    self.z_list.append(0)
                    self.gates_locations.append((int(x), int(y), 0))

                    # set boundaries of grid
                    if int(x) > self.max_x:
                       self.max_x = int(x)
                    if int(y) > self.max_y:
                        self.max_y = int(y)
                except ValueError:
                    pass
        return gates
