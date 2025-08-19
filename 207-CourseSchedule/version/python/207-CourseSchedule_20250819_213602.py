# Last updated: 8/19/2025, 9:36:02 PM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = self.createIndegree(numCourses , prerequisites)
        graph = self.createGraph(numCourses , prerequisites)

        queue = []
        visited = [False]*numCourses

        for i in range(len(indegree)) : 
            if indegree[i] == 0 : 
                queue.append(i)
        

        while len(queue) > 0 : 

            rem = queue.pop(0)
            visited[rem] = True

            nbrs = graph[rem]

            for n in nbrs : 
                indegree[n] -=1
                if indegree[n] == 0 : 
                    queue.append(n)
        
        for i in range (numCourses) : 
            if visited[i] == False : 
                return False
        
        return True
    

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