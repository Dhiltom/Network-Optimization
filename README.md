CSCE - 629 - Analysis of Algorithms

Course Project - Network Optimization

Dhiltom Pandaraparambil Antony

UIN : 327008700


The package for this particular project contains the following 7 files:
1. main.py               - Number of vertices, iterations and number of s-t pairs are set here
2. graph.py              - The graphs are generated here
3. algorithms.py         - Contains the 3 algorithms 
4. heap.py               - Contains the implementation of heap data structure
5. Results.txt           - The results that are printed during the execution of the program (contains only time taken for execution)
6. Results_Path.txt      - Contains the MBP path along with the time taken for execution
7. Report.pdf

Python version - Python 3.7.4

Command to run the program : python main.py

This command sets up boths the graphs with 5000 vertices and finds the Maximum Bandwidth path using the following 3 algorithms :
1) Modified Dijkstra's without heap
2) Modified Dijkstra's with heap data structure for fringes
3) Modified Kruskal's , where edges are sorted by HeapSort

The program is run for 5 pairs of source and destination vertices (s-t pairs) on each graph and this is done for 5 sets of graphs.
The program finally returns a consolidated output of the average time taken by each of the 3 above mentioned algorithms.


In main.py file, the following variables define the Number of vertices, iterations and number of s-t pairs and may be modified based on requirement:
1. num_of_vertices - Number of vertices
2. iterations      - Number of s-t (source-destination vertex) pairs
3. repeat          - Number of sets of graphs
 

The following 2 libraries are used in this project:
1. time      - to calculate the time taken for execution
2. random    - to get random values so that the graph generated will be random 

