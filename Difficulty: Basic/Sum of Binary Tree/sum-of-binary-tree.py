'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''        

class Solution:
    def sumBT(self, root):
        #code here
        if root is None : 
            return 0
        
        temp1 = self.sumBT(root.left)
        temp2 = self.sumBT(root.right)
        
        return temp1 + temp2 + root.data
        