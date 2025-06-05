class Solution:
    
    def topoSort(self, V, edges):
        # Code here
        indegree = [0]*V
        
        graph = self.constructGraph(edges , V)
        
        # for neighbours in range(len(graph)) : 
        #     for n in neighbour : 
        #         indegree[n] +=1
        
        for u , v in edges : 
            indegree[v] +=1
            
        result = []
        my_queue = []
        
        for i in range(len(indegree)) : 
            if indegree[i] == 0 : 
                my_queue.append(i)
                
        
        while len(my_queue) > 0 :
            temp = my_queue.pop(0)
            result.append(temp)
            
            neighbours = graph[temp]
            for n in neighbours : 
                indegree[n] -=1
                if indegree[n] == 0:
                    my_queue.append(n)
        
        return result
        
    def constructGraph(self , edges : list[list[int]], V : int) -> list[list[int]] : 
        
        adj = []
        
        for i in range (V) : 
            adj.append([])
            
        
        for u , v in edges : 
            adj[u].append(v)
        
        return adj
    