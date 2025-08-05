'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        result = self.helper(root)
        if result == 0 or result == -1 : 
            return 0
        return result
    
    def helper(self , root) : 
        if root is None : 
            return -1
        
        lht = self.helper(root.left)
        rht = self.helper(root.right)
        
        return max(lht , rht) + 1