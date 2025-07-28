'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

#Function to return a list containing elements of left view of the binary tree.
class Solution:
    def LeftView(self, root):
        # code here
        queue = []
        queue.append(root)
        result = []
        
        if root is None : 
            return result
        
        while len(queue) > 0 : 
            
            n = len(queue)
            for i in range(n) : 
                popped = queue.pop(0)
                
                if i == 0 and popped: 
                    result.append(popped.data)
                
                if popped.left : queue.append(popped.left)
                if popped.right : queue.append(popped.right)
        
        return result
            