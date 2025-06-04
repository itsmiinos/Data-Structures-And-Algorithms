class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
        # code here
        my_queue=[]
        result = []
        my_queue.append(adj[0])
        result.append(0)
        visited = [False]*(len(adj) + 1)
        visited[0] = True
        
        while len(my_queue) > 0 : 
            temp_list = my_queue.pop(0)
            
            for item in temp_list : 
                if visited[item] == False :
                    my_queue.append(adj[item])
                    visited[item] = True
                    result.append(item)
        return result
                