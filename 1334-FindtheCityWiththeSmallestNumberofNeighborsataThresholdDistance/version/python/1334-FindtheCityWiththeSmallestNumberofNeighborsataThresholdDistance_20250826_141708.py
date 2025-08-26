# Last updated: 8/26/2025, 2:17:08 PM
class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        adj = self.convertEdgesToAdj(edges , n)
        
        for k in range(n) : 
            for i in range(n) : 
                for j in range(n) : 
                    adj[i][j] = min(adj[i][j] , adj[i][k] + adj[k][j])
                    
                        
        min_count = float('inf')
        result = -1
        for i in range(n) : 
            count = 0
            for j in range(n) : 
                if adj[i][j] <= distanceThreshold :
                    count+=1
            
            if count <= min_count :
                min_count = count
                result = i
        
        return result
        
                
    

    def convertEdgesToAdj(self , edges : list[list[int]] , n : int) -> list[list[int]] : 

        adj = [[float('inf') for j in range (n)] for i in range(n)]

        for i in range(n):
            adj[i][i] = 0

        for u , v , w in edges : 
            adj[u][v] = w
            adj[v][u] = w
        
        return adj