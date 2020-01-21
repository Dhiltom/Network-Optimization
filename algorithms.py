
import heap as heap
import graph as g
import time

def print_path(s,t,dad,bw):
    l = []
    node = t
    tmp = ""
    max_bw = float('inf')
    while node != s:
        # print(node)
        x = node+1
        # if x in l:
            # print("\n\n  ERROR \n\n",x)
        # else:
            # l.append(x)
        if bw[node] < max_bw:
            max_bw = bw[node]
        tmp = "----|" + str(bw[node]) + "|---->" + str(x) +tmp
        node = dad[node]
    y = s+1    
    tmp = str(y) + tmp
    # print()
    # print(tmp)
    # print()
    # print("Maximum Bandwidth : ",max_bw)
    

    
def Dijkstra_MBP(G,s,t):
    
    adjacency_list = G[0]
    weight = G[1]

    num_of_vertices = len(adjacency_list)
    status = [-1 for i in range(num_of_vertices)] #-1 -> unseen , 0 -> fringe , 1 -> in tree
    bw = [ 0 for i in range(num_of_vertices)]
    dad = [ 0 for i in range(num_of_vertices)]
    
    status[s] = 1
    
    for w in adjacency_list[s]:
        w = w-1
        status[w] = 0
        bw[w] = weight[s][w]
        dad[w] = s
    
    while (status[t] != 1):
        
        #to find best fringe
        max_bw = 0
        index = -1
        for i in range(num_of_vertices):
            if (status[i] is 0) and (bw[i] > max_bw) :
                max_bw = bw[i]
                index = i
        
        u = index
        status[u]  = 1
        
        for v in adjacency_list[u]:
            v = v-1
            if status[v] == -1:
                status[v] = 0
                bw[v] = min(bw[u],weight[u][v])
                dad[v] = u
            
            elif (status[v] == 0) and (bw[v]< min(bw[u],weight[u][v])):
                dad[v] = u
                bw[v] = min(bw[u],weight[u][v])
        
    # print(dad)
    # print()
    # print(bw)
    print_path(s,t,dad,bw)
    result = [dad,bw] 
    return result
    
def Dijkstra_MBP_Heap(G,s,t):

    adjacency_list = G[0]
    weight = G[1]
    
    MaxHeap = heap.Heap()
    
    num_of_vertices = len(adjacency_list)
    status = [-1 for i in range(num_of_vertices)] #-1 -> unseen , 0 -> fringe , 1 -> in tree
    bw = [ 0 for i in range(num_of_vertices)]
    dad = [ 0 for i in range(num_of_vertices)]
    
    status[s] = 1
    
    
    for w in adjacency_list[s]:
        w = w-1
        status[w] = 0
        bw[w] = weight[s][w]
        dad[w] = s
        MaxHeap.INSERT(w,bw[w])
    
    while (status[t] != 1):
        
        u = MaxHeap.MAXIMUM()   
        status[u]  = 1
        MaxHeap.DELETE(1)
        # print(u)
        # print(MaxHeap.H)
        # print(MaxHeap.D)
        for v in adjacency_list[u]:
           
            v = v-1
            if status[v] == -1:
                status[v] = 0
                bw[v] = min(bw[u],weight[u][v])
                dad[v] = u
                MaxHeap.INSERT(v,bw[v])
            elif (status[v] == 0) and (bw[v]< min(bw[u],weight[u][v])):
                MaxHeap.DELETE(MaxHeap.P[v])
                dad[v] = u
                bw[v] = min(bw[u],weight[u][v])
                MaxHeap.INSERT(v,bw[v])
    
    # print(dad)
    # print()
    #print(dad,bw)
    print_path(s,t,dad,bw)
    result = [dad,bw] 
    return result
    
 
def Kruskal_MBP(G,s,t):
    t1 = time.time()
    adjacency_list = G[0]
    weight = G[1]
    
    num_of_vertices = len(adjacency_list)
    edges_wt = []
    di = {}
    for i in range(num_of_vertices):
        for j in range(len(adjacency_list[i])):
            u = i + 1
            v = adjacency_list[i][j]
            bw = weight[u-1][v-1]
            if (u,v,bw) not in di:
                edges_wt.append([u,v,bw])
                di[(u,v,bw)] = 1
                di[(v,u,bw)] = 1
                
    # print(edges_wt,di)          
    MaxHeap = heap.Heap2()
    
    t2 = time.time()
    
    res = MaxHeap.HeapSort(edges_wt)
    
    edges = res[0]
    weights = res[1]
    
    t3 = time.time()
    # print(edges)
    # print()
    # print(weights)
    
    dad = []
    rank = []
    
    def MakeSet(v):
        dad.append(0)
        rank.append(0)
    
    def Find(v):
        r = v
        l = []
        while dad[r] != 0 :
            l.append(r)
            r = dad[r]
        while l:
            a = l.pop()
            dad[a] = r  
        return r
    
    def Union(r1,r2):
        if rank[r1]>rank[r2]:
            dad[r2] = r1
        elif rank[r2]>rank[r1]:
            dad[r1] = r2
        elif rank[r2] == rank[r1]:
            dad[r2] = r1
            rank[r1] += 1
    
    V = []
    MST_adjacency_list = []
    
    for i in range(num_of_vertices+1):
        V.append(i)
        MST_adjacency_list.append(g.Vertex(i))
        
    MST = g.Graph_Kruskal()
    
    MST.add_vertices(MST_adjacency_list)
    
    for i in range(num_of_vertices+1):
        MakeSet(i)
    
    for i in edges:
        r1 = Find(i[0])
        r2 = Find(i[1])
        if r1 != r2:        
            Union(r1,r2)
            MST.add_edge(MST_adjacency_list[i[0]],MST_adjacency_list[i[1]])
    
    MST_adjacency_list1 = MST.adjacency_list()
    # print(MST.vertices)
    # print(MST_adjacency_list1)
    MST_adjacency_list1.pop(0)
    
    t4 = time.time()
    
    #BFS to find path from s to t
    
    status = [-1 for i in range(num_of_vertices)]
    d      = [ 0 for i in range(num_of_vertices)]
    bw     = [ 0 for i in range(num_of_vertices)]
    queue= []
    status[s] = 1
    queue.append(s)
    u = s
    
    while u != t:
    
        u = queue.pop(0)
        
        for v in MST_adjacency_list1[u]:
            v= v-1
            # print(u,v,MST_adjacency_list1[u],queue)
            if status[v] == -1:
                status[v] = 0
                d[v] = u
                bw[v] = weight[u][v]
                queue.append(v)
        status[u] = 1
    # print(status)
    # print(d,bw)    
    
    print_path(s,t,d,bw)
    t5 = time.time()

    # print("BFS        : ",t5-t4)
    # print("MUF        : ",t4-t3)
    # print("HeapSort   : ",t3-t2)
    # print("HeapInsert : ",t2-t1)