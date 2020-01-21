
import graph as g
import time
import random 
import algorithms as algo

num_of_vertices = 5000
print()
print("Number of Vertices : ",num_of_vertices)

iterations = 5  #  num of s-t pairs
repeat     = 5  #  num of graphs
count      = 0
decimal    = 10 #num of decimal places in time calculation 

s1 = [0 for i in range(repeat)]
s2 = [0 for i in range(repeat)]
s3 = [0 for i in range(repeat)]
s4 = [0 for i in range(repeat)]
s5 = [0 for i in range(repeat)]
s6 = [0 for i in range(repeat)]

while count<repeat:
    print()
    print()
    print("Iteration : ",count+1)
    print()
    index = count
    count += 1
    t1 = time.time()   
    G1 = g.graph1(num_of_vertices)
    t2 = time.time()
    G2 = g.graph2(num_of_vertices)
    t3 = time.time()
    
    print("Time to create Sparse Graph : ",round((t2-t1),decimal))
    print("Time to create Dense  Graph : ",round((t3-t2),decimal))

    nodes = []
    dijksta_res_wo_heap = []
    dijksta_res_heap = []
    kruskal_res = []

    for i in range(iterations):
        # print()
        # print("Iteration - ",i+1)
        # print()
        s = random.randint(1,num_of_vertices)
        t = random.randint(1,num_of_vertices)
        while s == t:
            s = random.randint(1,num_of_vertices)
            t = random.randint(1,num_of_vertices)
        s = s-1
        t = t-1
        t1 = time.time()
        algo.Dijkstra_MBP(G1,s,t)
        t2 = time.time()
        algo.Dijkstra_MBP(G2,s,t)
        t3 = time.time()
        algo.Dijkstra_MBP_Heap(G1,s,t)
        t4 = time.time()
        algo.Dijkstra_MBP_Heap(G2,s,t)
        t5 = time.time()
        algo.Kruskal_MBP(G1,s,t)
        t6 = time.time()
        algo.Kruskal_MBP(G2,s,t)
        t7 = time.time()

        nodes.append([s+1,t+1])
        dijksta_res_wo_heap.append([round(t2-t1,decimal),round(t3-t2,decimal)])
        dijksta_res_heap.append([round(t4-t3,decimal),round(t5-t4,decimal)])
        kruskal_res.append([round(t6-t5,decimal),round(t7-t6,decimal)])
       
    print()
    print()
    print("RESULTS for SPARSE GRAPH : ",count)
    print()
    print("Nodes\t\tDijkstra\t\tDijkstra_Heap\t\tKruskal")
    for i in range(iterations):
        tmp = str(nodes[i]) + "\t" + str(dijksta_res_wo_heap[i][0]) + "\t\t" + str(dijksta_res_heap[i][0]) + "\t\t" + str(kruskal_res[i][0])
        print(tmp)
        s1[index] = s1[index] + dijksta_res_wo_heap[i][0]
        s2[index] = s2[index] + dijksta_res_heap[i][0]
        s3[index] = s3[index] + kruskal_res[i][0]
    tmp = "Avg\t\t" + str(round((s1[index]/iterations),decimal)) + "\t\t" + str(round((s2[index]/iterations),decimal)) + "\t\t" + str(round((s3[index]/iterations),decimal))
    print(tmp)    
    print()    
    print()
    print("RESULTS for DENSE GRAPH : ",count)
    print()
    print("Nodes\t\tDijkstra\t\tDijkstra_Heap\t\tKruskal")
    
    for i in range(iterations):
        tmp = str(nodes[i]) + "\t" + str(dijksta_res_wo_heap[i][1]) + "\t\t" + str(dijksta_res_heap[i][1]) + "\t\t" + str(kruskal_res[i][1])
        print(tmp)
        s4[index] = s4[index] + dijksta_res_wo_heap[i][1]
        s5[index] = s5[index] + dijksta_res_heap[i][1]
        s6[index] = s6[index] + kruskal_res[i][1]
    tmp = "Avg\t\t" + str(round((s4[index]/iterations),decimal)) + "\t\t" + str(round((s5[index]/iterations),decimal)) + "\t\t" + str(round((s6[index]/iterations),decimal))
    print(tmp) 
    print()

print()
print("Consolidated RESULTS for SPARSE GRAPHS : ")
print()
print("Graph\t\tDijkstra\t\tDijkstra_Heap\t\tKruskal")
x1,x2,x3 = 0,0,0

for i in range(repeat):
    tmp = str(i+1) + "\t\t" + str(round((s1[i]/iterations),decimal)) + "\t\t" + str(round((s2[i]/iterations),decimal)) + "\t\t" + str(round((s3[i]/iterations),decimal))
    print(tmp)
    x1 = x1 + s1[i]/iterations
    x2 = x2 + s2[i]/iterations
    x3 = x3 + s3[i]/iterations

tmp = "Avg\t\t" + str(round((x1/repeat),decimal)) + "\t\t" + str(round((x2/repeat),decimal)) + "\t\t" + str(round((x3/repeat),decimal))
print(tmp)

print()
print("Consolidated RESULTS for DENSE GRAPHS : ")
print()
print("Graph\t\tDijkstra\t\tDijkstra_Heap\t\tKruskal")
x1,x2,x3 = 0,0,0

for i in range(repeat):
    tmp = str(i+1) + "\t\t" + str(round((s4[i]/iterations),decimal)) + "\t\t" + str(round((s5[i]/iterations),decimal)) + "\t\t" + str(round((s6[i]/iterations),decimal))
    print(tmp)
    x1 = x1 + s4[i]/iterations
    x2 = x2 + s5[i]/iterations
    x3 = x3 + s6[i]/iterations

tmp = "Avg\t\t" + str(round((x1/repeat),decimal)) + "\t\t" + str(round((x2/repeat),decimal)) + "\t\t" + str(round((x3/repeat),decimal))
print(tmp)