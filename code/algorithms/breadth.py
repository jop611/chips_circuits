import queue
from code.classes.netlist import *
from code.classes.print import *
from code.algorithms.constraints import *
from code.algorithms.helpers import *

def valid(grid, moves, start, end):
    start = start
    end = end


    for move in moves:
        if move == "L":
            start[0] -= 1

        elif move == "R":
            start[0] += 1

        elif move == "U":
            start[1] -= 1

        elif move == "D":
            start[1] += 1

        if not(0 <= start[0] < len(x-as) and 0 <= start[1] < len(y-as)):
            return False
        elif (start == obstacle):
            return False

    return True


def end(grid, moves, start, end):
    start = start
    end = end

    for move in moves:
        if move == "L":
            start[0] -= 1

        elif move == "R":
            start[0] += 1

        elif move == "U":
            start[1] -= 1

        elif move == "D":
            start[1] += 1

    if end == start:
        return True

    return False


# MAIN ALGORITHM
start = connection[0]
end = connection[1]
paths = queue.Queue()
paths.put("")
add = ""
grid  = #map met obstacles

while not end(grid, add, start, end):
    add = paths.get()

    for direction in ["L", "R", "U", "D"]:
        put = add + move
        if valid(grid, put):
            for move in moves:
                if move == "L":
                    start[0] -= 1

                elif move == "R":
                    start[0] += 1

                elif move == "U":
                    start[1] -= 1

                elif move == "D":
                    start[1] += 1

                paths.put(start)
