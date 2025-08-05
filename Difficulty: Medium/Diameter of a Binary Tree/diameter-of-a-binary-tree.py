'''
# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def diameter(self, root):
        # Your code here
        self.ans = float('-inf')
        self.calculateHeight(root)
        return self.ans
    
    def calculateHeight(self , root) :
        def helper(root) : 
            if root is None : 
                return -1
            
            lht = helper(root.left)
            rht = helper(root.right)
            
            self.ans = max(self.ans , lht + rht + 2)
            return max(lht , rht) + 1
        
        helper(root)
        
        