class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = self.convertToAdj(numCourses , prerequisites)

        indegree = [0]*(numCourses)
        visited = [False]*(numCourses)
        for u,v in prerequisites : 
            indegree[u] +=1
        
        my_queue = []
        for i in range(numCourses) : 
            if indegree[i] == 0 :
                my_queue.append(i)
        
        while len(my_queue) > 0 : 
            temp = my_queue.pop(0)
            visited[temp] = True
            neighbours = adj[temp]

            for n in neighbours : 
                indegree[n] -=1 
                if indegree[n] == 0 :
                    my_queue.append(n)
        
        for i in range (len(visited)) : 
            if visited[i] == False : 
                return False
        
        return True

    
    def convertToAdj(self , numCourses : int , prerequisites : list[list[int]]) -> list[list[int]] :
        result = []

        for i in range(numCourses) : 
            result.append([])

        for u,v in prerequisites : 
            result[v].append(u)

        return result