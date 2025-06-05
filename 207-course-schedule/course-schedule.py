class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        visited = [False]*numCourses
        for u,v in prerequisites : 
            indegree[v] +=1
        
        graph = self.constructGraph(numCourses , prerequisites)

        my_queue = []

        for i in range (len(indegree)) : 
            if indegree[i] == 0 : 
                my_queue.append(i)
        
        while len(my_queue) > 0 :
            temp = my_queue.pop(0)
            visited[temp] = True
            neighbours = graph[temp]

            for n in neighbours : 
                indegree[n] -=1
                if indegree[n] == 0 :
                    my_queue.append(n)
        
        for i in range (len(visited)) : 
            if visited[i] == False : 
                return False

        return True



    
    def constructGraph(self, num: int , prerequisites : list[list[int]]) -> list[list[int]] : 
        adj = []

        for i in range (num) : 
            adj.append([])
        
        for u , v in prerequisites : 
            adj[u].append(v)

        return adj