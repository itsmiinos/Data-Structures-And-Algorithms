class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        my_queue = []
        if n < 2 : 
            return True
        my_queue.append(source)
        visited = [False]*(n+1)
        adj = self.constructGraph(n , edges)
        while len(my_queue) > 0 :
            node = my_queue.pop(0)
            
            for neighbour in adj[node] :
                if visited[neighbour] == False : 
                    my_queue.append(neighbour)
                    visited[neighbour] = True
        return visited[destination]
    
    def constructGraph(self , n : int , edges : List[List[int]]) -> List[List[int]] :
        
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        return adj
        