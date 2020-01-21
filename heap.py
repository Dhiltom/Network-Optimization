
class Heap:

    def __init__(self):
        self.n = 0
        self.H = [-1] 
        self.D = [-1] #weight - bw
        self.P = {} #vertex - position mapping
        
    def MAXIMUM(self):
        return self.H[1]
    
    def INSERT(self,v,wt):
         
        self.H.append(v) 
        self.D.append(wt)
        self.n += 1
        self.P[v] = self.n
        self.HeapFy(self.n)

    def DELETE(self,k):
         
        tmp = self.H[k]
        self.H[k] = self.H[self.n]
        self.D[k] = self.D[self.n]
        self.P[self.H[self.n]] = self.P[tmp]
        self.H.pop()
        self.D.pop()
        del self.P[tmp]
        self.n -= 1
      
        if k<=self.n:
            self.HeapFy(k)
        
    def HeapFy(self,k):
        
        
        if k>1 and self.D[k]>self.D[k//2]:
            h=k
            while h>1 and self.D[h]>self.D[h//2]:
                self.swap(h,h//2)
                h = h//2
        elif (k<=self.n/2) and (((2*k+1)<=self.n and (self.D[k]< max(self.D[2*k],self.D[2*k+1]))) or (2*k<=self.n and self.D[k]<self.D[2*k])):
            h=k
            while (h<=self.n/2) and (((2*h+1)<=self.n and (self.D[h]< max(self.D[2*h],self.D[2*h+1]))) or (2*h<=self.n and self.D[h]<self.D[2*h])) :
                if 2*h+1<=self.n:
                    if self.D[2*h]>self.D[2*h+1]:
                        d = 2*h
                    else:
                        d = 2*h+1
                else:
                    d = 2*h
                self.swap(h,d)
                h = d

    def swap(self,a,b):
        
        tmp = self.D[a]
        self.D[a] = self.D[b]
        self.D[b] = tmp
        
        tmpA = self.H[a]
        tmpB = self.H[b]
        self.H[a] = self.H[b]
        self.H[b] = tmpA
        
        tmp = self.P[tmpA]
        self.P[tmpA] = self.P[tmpB]
        self.P[tmpB] = tmp
     
    
class Heap2:

        def heapify(self,heaplist, n, i): 
            smallest = i  
            l = 2 * i + 1     # left = 2*i + 1 
            r = 2 * i + 2     # right = 2*i + 2 
          
            if l < n and heaplist[i][2] > heaplist[l][2]: 
                smallest = l 
          
            if r < n and heaplist[smallest][2] > heaplist[r][2]: 
                smallest = r 
          
            # Change root, if needed 
            if smallest != i: 
                heaplist[i],heaplist[smallest] = heaplist[smallest],heaplist[i] # swap 
          
                # Heapify the root. 
                self.heapify(heaplist, n, smallest) 
            
        def HeapSort(self,heaplist): 
            n = len(heaplist) 
            
            # Build a minheap. 
            for i in range(n, -1, -1): 
                self.heapify(heaplist, n, i) 
            
            # One by one extract elements 
            for i in range(n-1, 0, -1): 
                heaplist[i], heaplist[0] = heaplist[0], heaplist[i] # swap 
                self.heapify(heaplist, i, 0) 
            
            edges = []
            weights = []
            for i in range(n):
                
                edges.append([heaplist[i][0],heaplist[i][1]])
                weights.append(heaplist[i][2])
                
            result = [edges,weights]
            return result