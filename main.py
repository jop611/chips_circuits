from code.classes.netlist import Netlist
from code.algorithms.breadthfirst import BreadthFirst
from code.algorithms.a_star import A_Star
from code.algorithms.hillclimber import HillClimber


def main():
    algorithm = input(f"\nChoose algorithm to perform\n"
                       "***************************\n\n"
                       "Options:\n"
                       "A: A* algorithm\n"
                       "B: Breadth-first search algorithm\n"
                       "C: Hillclimber algorithm on previously found solution\n").upper()
                       
                       
    # choice of print can be either 1 or 2
    print_nr = input(f"\nChoose a print to use (1/2): ")


    # for print 1, options are 0-3. netlist 0 is a simple netlist for testing purposes.
    # for print 2, options are 4-6. 
    netlist_nr = input("Choose a netlist to solve (0-6): ")
       

    # a_star is the main algorithm that is guaranteed to solve netlist 0-5 in a matter of minutes.
    # no solution is currently known for netlist 6.
    if algorithm == "A":
        a_star = A_Star(print_nr, netlist_nr)
        a_star.run()
    

    # breadth first search suffices for netlist 0 but is not recommended for more complex netlists
    elif algorithm == "B":
        bfs = BreadthFirst(print_nr, netlist_nr)
        bfs.run()


    # hillclimber algorithm can be used on obtained results. it requires the correct length of the result to be improved as input.
    # options: 409 for netlist 0, 709 for netlist 1, 1047 for netlist 2, 
    #          1219 for netlist 3, 1460 for netlist 4, 1610 for netlist 5.
    elif algorithm == "C":
        length = input("Length of solution to perform hillclimber on: ")
        hillclimber = HillClimber(print_nr, netlist_nr, length)
        hillclimber.run()


if __name__ == "__main__":
    main()

    
    
