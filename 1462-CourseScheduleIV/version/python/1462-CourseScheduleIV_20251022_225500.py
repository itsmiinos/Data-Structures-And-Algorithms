# Last updated: 10/22/2025, 10:55:00 PM
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = self.createGraph(numCourses , prerequisites)
        map = {} # course -> set()

        for i in range(numCourses) : 
            if i not in map :
                visited = [False]*numCourses
                dependents = set()
                self.doDFS(graph , i , visited , dependents)
                map[i] = dependents

        result = []
        
        for u , v in queries : 
            dependents = map[u]
            if v in dependents :
                result.append(True)
            else : 
                result.append(False)
        
        return result
    
    def doDFS(self , graph : list[list[int]] , src : int , visited : list[bool] , dependents : list[int]) -> list[int] : 

        visited[src] = True

        for nei in graph[src] : 
            if visited[nei] == False : 
                dependents.add(nei)
                self.doDFS(graph , nei , visited , dependents)
        
        return dependents

    
    def createGraph(self , numCourses : int , prerequisites : list[list[int]]) -> list[int] :
        graph = []

        for i in range(numCourses) : 
            graph.append([])
        
        for u , v in prerequisites : 
            graph[u].append(v)
        
        return graph
