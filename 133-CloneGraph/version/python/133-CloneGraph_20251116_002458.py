# Last updated: 11/16/2025, 12:24:58 AM
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
        map = {} #taking map for not calling duplicate node

        if node is None : 
            return None
        
        return self.solve(node , map)
    
    def solve(self , node : 'Node' , map : tuple) -> 'Node' :
        if node is None : 
            return None
        
        if node in map : 
            return map[node]
        
        clone = Node(node.val)
        map[node] = clone
        nei = node.neighbors

        for n in nei : 
            clone.neighbors.append(self.solve(n , map))
        
        

        return clone
