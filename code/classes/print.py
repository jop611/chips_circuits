from code.classes.netlist import *


class Print():
    def __init__(self, print_nr):
        self.max_x = 0
        self.max_y = 0
        self.max_z = 7
        self.x_list = []
        self.y_list = []
        self.z_list = []
        self.chips = self.load_print(print_nr)
        self.chips_locations = []
        self.boundaries = ((0, 0, 0), (self.max_x + 1, self.max_y + 1, 7))
        
        print(self.boundaries)

    def load_print(self, print_nr):
        chips = {}

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

        