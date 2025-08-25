# Last updated: 8/25/2025, 7:59:33 PM
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outdegree = self.calculateOutdegree(graph)
        parent = self.calculateParent(graph)
        result = []
        queue = []

        for i in range(len(outdegree)) : 
            if outdegree[i] == 0 : 
                queue.append(i)
        
        while len(queue) > 0 : 
            rem = queue.pop(0)
            result.append(rem)

            pars = parent[rem]
            for p in pars : 
                outdegree[p] -=1
                if outdegree[p] == 0 : 
                    queue.append(p)
        result.sort()
        return result
    
    def calculateParent(self , graph : list[list[int]]) -> list[list[int]] :

        parent = [[] for _ in range(len(graph))]

        for i in range(len(graph)) :
            for j in graph[i] :
                parent[j].append(i)
        
        return parent


    def calculateOutdegree(self , graph : list[list[int]]) -> list[int] :

        outdegree = [0] * len(graph)

        for i in range (len(graph)) :
            outdegree[i] += len(graph[i])
        
        return outdegree