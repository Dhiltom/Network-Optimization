
import random
import time

class Vertex:

    def __init__(self,vertex):
        self.id = vertex
        self.next = []

    def add_neighbor(self,neighbor):
        if neighbor.id not in self.next:
                self.next.append(neighbor.id)
                neighbor.next.append(self.id)
                self.next = sorted(self.next)
                neighbor.next = sorted(neighbor.next)
 
                
class Graph:

    def __init__(self,n):
        self.vertices = {}
        self.adjacency_matrix = [[ 0 for i in range(n)] for j in range(n)]
        
    def add_vertices(self, vertices):
        for vertex in vertices:
            if isinstance(vertex, Vertex):
                self.vertices[vertex.id] = vertex.next
		
    def add_edge(self,vertex_A,vertex_B,i,j):
        self.adjacency_matrix[i-1][j-1] = self.adjacency_matrix[j-1][i-1] = random.randint(1,1000)
        vertex_A.add_neighbor(vertex_B)        
        self.vertices[vertex_A.id] = vertex_A.next
        self.vertices[vertex_B.id] = vertex_B.next
    
    def adjacency_list(self): 
        return [self.vertices[key] for key in self.vertices.keys()] 


#same graph but without the weight
class Graph_Kruskal: 

    def __init__(self):
        self.vertices = {}

    def add_vertices(self, vertices):
        for vertex in vertices:
            if isinstance(vertex, Vertex):
                self.vertices[vertex.id] = vertex.next
                
    def add_edge(self,vertex_A,vertex_B):
        if isinstance(vertex_A, Vertex) and isinstance(vertex_B, Vertex):
            vertex_A.add_neighbor(vertex_B)        
            self.vertices[vertex_A.id] = vertex_A.next
            self.vertices[vertex_B.id] = vertex_B.next
            
    def adjacency_list(self): 
        return [self.vertices[key] for key in self.vertices.keys()]
    

def graph2(num_of_vertices):
    
    V = []
    adjacency_list = []
    adjacency_list.append(0)
    for i in range(1,num_of_vertices+1):
        V.append(i)
        adjacency_list.append(Vertex(i))
        
    graph = Graph(num_of_vertices)
    
    graph.add_vertices(V)
    
    edge_count = 0
    
    for i in range(1,num_of_vertices):
        graph.add_edge(adjacency_list[i],adjacency_list[i+1],i,i+1)
        edge_count+=1
        
    graph.add_edge(adjacency_list[num_of_vertices],adjacency_list[1],num_of_vertices,1)
    edge_count+=1
    
    for i in range(1,num_of_vertices+1):
        for j in range(i+2,num_of_vertices+1):
            
            if (random.randint(1,100)) <= 20:
                graph.add_edge(adjacency_list[i],adjacency_list[j],i,j)
                edge_count+=1
                
    adj_list = graph.adjacency_list()
    adj_mat = graph.adjacency_matrix
    # print(adj_list)
    #print()
    # print(adj_mat)
    #print()
    print("Dense  Graph edge count : ",edge_count)
    output = [adj_list,adj_mat]
    return output
    

def graph1(num_of_vertices):
    
    V = []
    adjacency_list = []
    adjacency_list.append(0)
    for i in range(1,num_of_vertices+1):
        V.append(i)
        adjacency_list.append(Vertex(i))
        
    graph = Graph(num_of_vertices)
    
    graph.add_vertices(V)
    
    edge_count = 0
    list_of_edges = {}
    for i in range(1,num_of_vertices):
        graph.add_edge(adjacency_list[i],adjacency_list[i+1],i,i+1)
        edge_count+=1
        list_of_edges[(i,i+1)] = 1
        list_of_edges[(i+1,i)] = 1
        
    graph.add_edge(adjacency_list[num_of_vertices],adjacency_list[1],num_of_vertices,1)
    edge_count+=1
    list_of_edges[(num_of_vertices,1)] = 1
    list_of_edges[(1,num_of_vertices)] = 1
    
    
    
    #avg_vertex_degree = 6
    #total_edges = (avg_vertex_degree/2) * num_of_vertices
    count = 1
    for i in range(1,num_of_vertices+1):      
        while count<=2:
            j = random.randint(1,num_of_vertices)     
            if [(i,j) not in list_of_edges] and (i != j):
                
                graph.add_edge(adjacency_list[i],adjacency_list[j],i,j)
                edge_count+=1
                count+=1
                list_of_edges[(i,j)] = 1
                list_of_edges[(j,i)] = 1
                
        count = 1
       
    adj_list = graph.adjacency_list()
    adj_mat = graph.adjacency_matrix
    #print(adj_list)
    #print()
    #print(adj_mat)
    #print()
    print("Sparse Graph edge count : ",edge_count)
    output = [adj_list,adj_mat]
    return output

