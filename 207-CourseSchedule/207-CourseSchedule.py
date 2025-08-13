# Last updated: 8/13/2025, 8:21:15 PM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = self.calculateIndegree(numCourses , prerequisites)
        neighbours = self.calculateNeighbours(numCourses , prerequisites)
        visited = [False]*numCourses
        
        my_queue = []
        for i in range(len(indegree)) : 
            if indegree[i] == 0 :
                my_queue.append(i)
        
        while len(my_queue) > 0 : 
            popped = my_queue.pop(0)
            
            visited[popped] = True
            neighbour = neighbours[popped]

            for n in neighbour : 
                indegree[n]-=1
                if indegree[n] == 0 : 
                    my_queue.append(n)
        
        for i in range(len(visited)) : 
            if visited[i] == False : 
                return False
        
        return True
        


    def calculateIndegree(self , numCourses : int , prerequisites : List[List[int]]) -> [int] : 

        indegree = [0]*numCourses

        for u , v in prerequisites : 
            indegree[u] +=1
        
        return indegree
    
    def calculateNeighbours(self , numCourses : int , prerequisites : List[List[int]]) -> List[List[int]] : 

        neighbours = [None]*numCourses

        for i in range(numCourses) : 
            neighbours[i] = []
        
        for u , v in prerequisites : 
            neighbours[v].append(u)
        
        return neighbours