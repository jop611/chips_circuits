### Explanation of folder
You can find several pathfinding algorithms in this folder.
The **breadthfirst** algorithm tries to find a path by checking every possible option beginning from the node. 
The **a-star** algorithm finds his way through the grid by looking at his neighbours. Some neighbours are more favorable moving to then others & the algorithm is designed to move to the most favourable neighbour. 
The **hillclimber** algorithm is designed to act after a netlist is succesfully connected. The **hillclimber** algorithm breaks every connection step by step & tries to make a shorter connection without the use of some heuristics used in the **a-star** algorithm.
For more information on the algorithms, you can click the algorithm files & read the docstrings.