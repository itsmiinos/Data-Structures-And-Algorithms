# Last updated: 10/22/2025, 8:42:50 PM
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = self.createIndegree(numCourses , prerequisites)
        graph = self.createGraph(numCourses , prerequisites)

        result = []

        queue = []
        visited = [False]*numCourses

        for i in range(len(indegree)) : 
            if indegree[i] == 0 : 
                queue.append(i)
        

        while len(queue) > 0 : 

            rem = queue.pop(0)
            result.append(rem)
            visited[rem] = True

            nbrs = graph[rem]

            for n in nbrs : 
                indegree[n] -=1
                if indegree[n] == 0 : 
                    queue.append(n)
        
        if len(result) == numCourses:
            return result
        return []
    

    def createGraph(self , numCourses : int , prerequisites : list[list[int]]) -> list[list[int]] : 

        graph = []

        for i in range(numCourses) : 
            graph.append([])
        
        for u , v in prerequisites : 
            graph[v].append(u)
        
        return graph

    
    def createIndegree(self , numCourses : int , prerequisites : list[list[int]]) -> list[int] :

        indegree = [0]*numCourses

        for u , v in prerequisites : 
            indegree[u]+=1
        
        return indegree