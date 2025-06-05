#User function Template for python3

class Solution:
    def numProvinces(self, adj, V):
        # code here 
        n = len(adj)
        visited_array = [False]*n
        ans = 0
        
        for i in range(V) : 
            if visited_array[i] == False : 
                self.dfsHelper(adj , visited_array , i)
                ans +=1
        
        return ans
                
        
    def dfsHelper(self, adj : list[list[int]] , visited_array : [bool] , src : int) :
        
        visited_array[src] = True
        for neighbor in range(len(adj)):
            if adj[src][neighbor] == 1 and not visited_array[neighbor]:
                self.dfsHelper(adj, visited_array, neighbor)
    