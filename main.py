"""
main.py

Interface for running the program

(C) 2020 Teamname, Amsterdam, The Netherlands
"""

from code.classes.netlist import Netlist
from code.algorithms.breadth import bfs
from code.algorithms.a_star import a_star
from code.algorithms.hillclimber import hillclimber
from visualize import plot


def main():
    algorithm = input(f"\nChoose algorithm to perform\n"
                       "***************************\n\n"
                       "Options:\n"
                       "A: A* algorithm\n"
                       "B: Breadth-first search algorithm\n"
                       "C: Hillclimber algorithm on previously found solution\n").upper()

    print_nr = int(input("Choose a print to use: "))
    netlist_nr = int(input("Choose a netlist to solve (0-6): "))

    netlist = Netlist(print_nr, netlist_nr)

    if algorithm == "A":
        while not a_star(netlist):
            pass
    elif algorithm == "B":
        while not bfs(netlist):
            pass
    elif algorithm == "C":
        hillclimber(netlist)

    plot(netlist.print.x_list, netlist.print.y_list, netlist.print.z_list, netlist.print.boundaries, netlist.path_plot, netlist.length)

if __name__ == "__main__":
    main()
