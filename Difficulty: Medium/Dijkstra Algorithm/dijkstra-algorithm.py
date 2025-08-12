import heapq

class Pair : 
    def __init__(self , wt = None , v = None) : 
        self.wt = wt
        self.v = v
    def __lt__(self, other):
        return self.wt < other.wt
        
        
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        graph = self.createGraph(edges , V)
        heap = []
        ans = [float('inf')]*V
        heapq.heappush(heap , Pair( 0 , src))
        
        while len(heap) > 0 : 
            rem = heapq.heappop(heap)
            
            if rem.wt > ans[rem.v]:
                continue
            ans[rem.v] = min(ans[rem.v] , rem.wt)
            
            nbrs = graph[rem.v]
            for n in nbrs : 
                new_dist = rem.wt + n.wt
                if new_dist < ans[n.v]:
                    ans[n.v] = new_dist
                    heapq.heappush(heap, Pair(new_dist , n.v))
        
        return ans
        
        
    
    def createGraph(self , edges : list[list[int]] , V : int) -> list[list[Pair]] : 
        
        graph = []
        
        for i in range(V) : 
            graph.append([])
        
        for i in range(len(edges)) : 
            u = edges[i][0]
            v = edges[i][1]
            wt = edges[i][2]
            
            graph[u].append(Pair(wt , v))
        
        return graph
            
            
