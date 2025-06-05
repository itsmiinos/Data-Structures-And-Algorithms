class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        # code here
        n = len(adj)
        visited_array = [False]*n
        result = []
        result.append(0)
        visited_array[0] = True
        self.DFShelper(adj , visited_array , 0 , result)
        return result
    
    def DFShelper(self , adj : list[list[int]] , visited_array : [bool] , src : int , result : [int]) :
        
        neighbours = adj[src]
        
        for n in neighbours : 
            if visited_array[n] == False :
                result.append(n)
                visited_array[n] = True
                self.DFShelper(adj , visited_array , n , result)