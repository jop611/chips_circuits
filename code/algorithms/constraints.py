
def check_for_chip(self, next_coor):
    for key in self.gates:
        if next_coor in self.gates[key]:
            return True
    return False

def check_for_right_chip(self, next_coor, destination):
    if next_coor == destination:
        return True
    return False