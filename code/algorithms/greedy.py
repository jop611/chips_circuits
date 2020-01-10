from code.classes.netlist import *

def connect(self, connection):
    self.path[connection] = []
    chip_a = connection[0]
    chip_b = connection[1]

    x_a = self.print.chips[chip_a][0]
    y_a = self.print.chips[chip_a][1]
    x_b = self.print.chips[chip_b][0]
    y_b = self.print.chips[chip_b][1]

    diff_x = x_b - x_a
    diff_y = y_b - y_a

    while x_a != x_b or y_a != y_b:
        if diff_x < 0:
            x_a -= 1
            diff_x = x_b - x_a 
        elif diff_x > 0:
            x_a += 1  
            diff_x = x_b - x_a     
        elif diff_y < 0:
            y_a -= 1
            diff_y = y_b - y_a
        elif diff_y > 0:
            y_a += 1
            diff_y = y_b - y_a

        self.path[connection].append((x_a, y_a))

def score():
    score = 0
    for connection in netlist.netlist:
        score += int(connection[2])
    return score