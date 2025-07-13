class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        start = 0
        my_queue = []
        result = []
        visited = [False]*len(adj)
        visited[start] = True
        my_queue.append(start)
        
        while len(my_queue) > 0 : 
            popped = my_queue.pop(0)
            result.append(popped)
            neigh = adj[popped]
            
            for n in neigh : 
                if visited[n] == False : 
                    visited[n] = True
                    my_queue.append(n)
        
        return result