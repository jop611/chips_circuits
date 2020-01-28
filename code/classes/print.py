"""
print.py

Print the grid with all netlist points

(C) 2020 Teamname, Amsterdam, The Netherlands
"""

from code.classes.netlist import *

class Print():
    def __init__(self, print_nr):
        self.max_x = 0
        self.max_y = 0
        self.max_z = 7
        self.x_list = []
        self.y_list = []
        self.z_list = []
        self.chips_locations = []
        self.chips = self.load_print(print_nr)
        self.boundaries = ((0, 0, 0), (self.max_x + 1, self.max_y + 1, 7))
        self.chip_count = len(self.chips)


    def load_print(self, print_nr):
        """Load chips in grid"""
        chips = {}

        # open csv file with gate coordinates
        with open(f'gates&netlists/chip_{print_nr}/print_{print_nr}.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for chip, x, y in reader:
                try:
                    chips[int(chip)] = (int(x), int(y), 0)
                    self.x_list.append(int(x))
                    self.y_list.append(int(y))
                    self.z_list.append(0)
                    self.chips_locations.append((int(x), int(y), 0))

                    # set boundaries of grid
                    if int(x) > self.max_x:
                       self.max_x = int(x)
                    if int(y) > self.max_y:
                        self.max_y = int(y)
                except ValueError:
                    pass
        return chips
