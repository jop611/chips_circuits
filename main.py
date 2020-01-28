from code.classes.netlist import Netlist
from code.algorithms.breadthfirst import BreadthFirst
from code.algorithms.a_star import A_star
from code.algorithms.hillclimber import Hillclimber
from code.algorithms.breadthfirst import BreadthFirst



def main():

    algorithm = input(f"\nChoose algorithm to perform\n"
                       "***************************\n\n"
                       "Options:\n"
                       "A: A* algorithm\n"
                       "B: Breadth-first search algorithm\n"
                       "C: Hillclimber algorithm on previously found solution\n").upper()

    print_nr = int(input("Choose a print to use (1/2): "))
    netlist_nr = int(input("Choose a netlist to solve (0-6): "))
   
    netlist = Netlist(print_nr, netlist_nr)
    
    
    if algorithm == "A":
        a_star = A_star(print_nr, netlist_nr)
        a_star.run()
    
    elif algorithm == "B":
        bfs = BreadthFirst(print_nr, netlist_nr)
        bfs.run()

    elif algorithm == "C":
        hillclimber = Hillclimber(print_nr, netlist_nr)
        hillclimber.run()


if __name__ == "__main__":
    main()

    
    
