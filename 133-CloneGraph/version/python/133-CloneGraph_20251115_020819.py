# Last updated: 11/15/2025, 2:08:19 AM
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        map = {}

        if node is None : 
            return None


        return self.dfs(node , map)
    
    def dfs(self , node : 'Node' , map : tuple) -> 'Node' : 
        if node in map : 
            return map[node]
        
        copy_node = Node(node.val)
        map[node] = copy_node
        neighbours = node.neighbors

        for n in neighbours : 
            copy_node.neighbors.append(self.dfs(n , map))
        
        return copy_node