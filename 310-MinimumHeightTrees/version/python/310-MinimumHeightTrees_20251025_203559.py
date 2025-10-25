# Last updated: 10/25/2025, 8:35:59 PM
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = self.createIndegreeArray(edges , n)
        neighbours = self.createNeighboursArray(edges , n)

        if not edges : 
            return [0]


        total_nodes = n
        queue = []

        for i in range(n) : 
            if indegree[i] == 1 : 
                queue.append(i)
        
        while len(queue) > 0 : 
            level = len(queue)

            if total_nodes == level == 2 or total_nodes == level == 1:
                break

            while level > 0 : 
                curr = queue.pop(0)
                total_nodes -=1
                nei = neighbours[curr]

                for n in nei : 
                    indegree[n] -=1
                    if indegree[n] == 1 : 
                        queue.append(n)
            
                level -=1
        
        return queue

    
    def createNeighboursArray(self , edges : list[list[int]] , n : int) -> list[list[int]] : 
        neighbours = []

        for i in range(n) : 
            neighbours.append([])
        
        for u , v in edges : 
            neighbours[u].append(v)
            neighbours[v].append(u)

        return neighbours

    
    def createIndegreeArray(self , edges : list[list[int]] , n : int) -> list[int] : 
        indegree = [0]*n

        for u , v in edges : 
            indegree[u] +=1
            indegree[v] +=1
        
        return indegree