# Last updated: 11/5/2025, 10:09:55 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

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
    