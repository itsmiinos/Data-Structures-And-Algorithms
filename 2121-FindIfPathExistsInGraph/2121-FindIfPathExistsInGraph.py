# Last updated: 8/13/2025, 8:16:34 PM
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adj = self.convertToAdjMatrix(n , edges)
        
        visited = [False]*(len(adj))
        my_queue = []
        my_queue.append(adj[0])
        visited[0] = True

        while len(my_queue) > 0 : 
            neighbours = my_queue.pop(0)

            for n in neighbours : 
                if visited[n] != True : 
                    my_queue.append(adj[n])
                    visited[n] = True
        
        return visited[source] and visited[destination]
    
    def convertToAdjMatrix(self , n : int , edges : List[List[int]]) -> List[List[int]]: 
        adj = []

        for i in range (n) : 
            adj.append([]) #intializing list of list
        
        for u,v in edges : 
            adj[u].append(v)
            adj[v].append(u)
        
        return adj