# Last updated: 10/24/2025, 10:04:24 PM
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph , possible_nodes = self.createGraph(equations , values)

        result = []

        for i in range(len(queries)) : 
            u = queries[i][0]
            v = queries[i][1]

            if u not in possible_nodes or v not in possible_nodes : 
                result.append(-1.0)
            else : 
                visited = set()
                ans = self.doDFS(u , v , graph , visited )
                result.append(ans)
        
        return result
    
    def doDFS(self , u : str , v : str , graph : tuple[str , list[str , int]] , visited : list[str]) -> int : 

        if u == v : 
            return 1.0
     
        visited.add(u)

        neighbours = graph[u]

        for nei , weight in neighbours : 
            if nei not in visited :
                val =  self.doDFS(nei , v , graph , visited)
                if val != -1 : 
                    return weight * val
        
        return -1


    def createGraph(self , equations : list[list[int]] , values : list[list[int]] ) : 
        graph = {}
        possible_nodes = {}
        
        for i in range(len(equations)) : 
            u = equations[i][0]
            v = equations[i][1]
            w = values[i]

            if u in graph : 
                graph[u].append([v , w])
            else : 
                graph[u] = []
                graph[u].append([v , w])
            
            if u in possible_nodes : 
                possible_nodes[u].add(v)
            else : 
                possible_nodes[u] = set()
                possible_nodes[u].add(v)
            
            if v in graph : 
                graph[v].append([u , float(1/w)])
            else : 
                graph[v] = []
                graph[v].append([u , float(1/w)])
            
            if v in possible_nodes : 
                possible_nodes[v].add(u)
            else : 
                possible_nodes[v] = set()
                possible_nodes[v].add(u)
        
        return graph , possible_nodes

        