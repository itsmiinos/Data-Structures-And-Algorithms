# Last updated: 8/18/2025, 11:57:17 PM
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = self.createGraph(edges , n)

        visited = [False]*n
        visited[source] = True

        self.doDFS(graph , source , visited)

        return visited[source] and visited[destination]


    
    def doDFS(self , graph : list[list[int]] , source : int , visited : list[bool]) -> None : 

        nbrs = graph[source]

        for n in nbrs : 
            if visited[n] == False : 
                visited[n] = True
                self.doDFS(graph  , n , visited)
    

    def createGraph(self , edges : list[list[int]] , n : int) -> list[list[int]] :

        graph = []

        for i in range(n) : 
            graph.append([])
        
        for u , v in edges : 
            graph[u].append(v)
            graph[v].append(u)
        
        return graph