# Chips & Circuits
Finding the shortest wiring pattern for a chip with fixed gates on a seven layered grid. The connections that have to be made between gates are given in netlists. The wires may not touch each other.

## Prerequisites
This code has been written in [Python3.7.5](https://www.python.org/downloads/). In requirements.txt are all the required packages to successfully use the code.

## Structure
All Python scripts are in the folder code. In the map gates&netlists are the chips with their netlists and gates position. The map results has all the given results saved.

## Algorithms
For this problem 3 algorithms were used:
* A*
* Hillclimber
* Breadth First

Hillclimber improves the solution found by A*.

## Testing
To use this code you first run:
```bash
python main.py
```
After choosing your preferred algorithm and netlist the code will search for a solution. If the choice was A* you can run the code again and chose Hillclimber as algorithm for a better solution.

At the end of each search a window will pop up with a visualisation of the found solution.

## Authors
Robel Haile, Jop Meijer & Navisa Rajabali

## Acknowledgments
Minor programming of the UvA

© 2019 All Rights Reserved
