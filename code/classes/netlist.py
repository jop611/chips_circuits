import csv

class Netlist():
    def __init__(self, print_nr, netlist_nr):
        self.gates = {}
        self.path = {}
        self.max_x = 0
        self.max_y = 0

        # map x, y coordinates of chips
        self.load_print(print_nr, netlist_nr)
            
        self.boundaries = ((0, 0), (self.max_x + 1, self.max_y + 1))
        print(self.boundaries)
        
        self.connections = []
        with open(f'gates&netlists/chip_{print_nr}/netlist_{netlist_nr}.csv', newline='') as csvfile:
            netlist = csv.reader(csvfile)
            for chip_a, chip_b in netlist:
                try:
                    manhattan_distance = abs(self.gates[int(chip_b)][0] - self.gates[int(chip_a)][0]) + abs(self.gates[int(chip_b)][1] - self.gates[int(chip_a)][1])
                    self.connections.append((int(chip_a), int(chip_b), manhattan_distance))
                except ValueError:
                    pass
            self.connections.sort(key=lambda connection: connection[2])
        print(self.connections)
        print()

    def load_print(self, print_nr, netlist_nr):

        with open(f'gates&netlists/chip_{print_nr}/print_{print_nr}.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for chip, x, y in reader:
                try:
                    self.gates[int(chip)] = (int(x), int(y))

                    # set boundaries of grid
                    if int(x) > self.max_x:
                       self.max_x = int(x)
                    if int(y) > self.max_y:
                        self.max_y = int(y) 
                except ValueError:
                    pass
    
    
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
                if not self.check_for_chip((x_a - 1, y_a)):
                    x_a -= 1
            elif diff_x > 0:
                self.check_for_chip((x_a + 1, y_a))
                x_a += 1       
            elif diff_y < 0:
                self.check_for_chip((x_a, y_a - 1))
                y_a -= 1
            elif diff_y > 0:
                self.check_for_chip((x_a, y_a + 1))
                y_a += 1

            self.path[connection].append((x_a, y_a))

        print(self.path[connection])

    def check_for_chip(self, next_coor):
        for key in self.gates:
            if next_coor in self.gates[key]:
                return True
        return False
    
    def check_for_right_chip(self, next_coor, destination):
        if next_coor == destination:
            return True
        return False

