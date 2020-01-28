from code.classes.netlist import Netlist
from code.algorithms.breadth import bfs
from code.algorithms.a_star_copy import A_star
from code.algorithms.hillclimber_copy import Hillclimber
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
        a_star = A_star(print_nr, netlist_nr)
        a_star.run()
            
    elif algorithm == "B":
        bfs(netlist)
        netlist.clear()
    elif algorithm == "C":
        hillclimber = Hillclimber(print_nr, netlist_nr)
        hillclimber.run()

    plot(a_star.netlist.print.x_list, a_star.netlist.print.y_list, a_star.netlist.print.z_list, a_star.netlist.print.boundaries, a_star.netlist.path_plot, a_star.netlist.length)

if __name__ == "__main__":
    main()

    
    
