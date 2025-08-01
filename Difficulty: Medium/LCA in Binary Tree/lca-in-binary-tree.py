'''
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    def lca(self,root, n1, n2):
        # Code here
        
        if root is None : 
            return root
        
        if root.data == n1 or root.data == n2 : 
            return root
        
        l = self.lca(root.left , n1 , n2)
        r = self.lca(root.right , n1 , n2)
        
        if l is not None and r is not None : 
            return root
        
        if l is None and r is not None : 
            return r
        
        if l is not None and r is None : 
            return l
        
        return None
        
        

