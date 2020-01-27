import random

def randomize(netlist):
    # randomly chosing a tuple and returning it
    connection = random.choice(netlist)
    return connection