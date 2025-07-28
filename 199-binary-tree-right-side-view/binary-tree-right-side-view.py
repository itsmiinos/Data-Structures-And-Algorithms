# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = []
        queue.append(root)
        result = []
        
        if root is None : 
            return result
        
        while len(queue) > 0 : 
            
            n = len(queue)
            for i in range(n) : 
                popped = queue.pop(0)
                
                if i == n-1 and popped: 
                    result.append(popped.val)
                
                if popped.left : queue.append(popped.left)
                if popped.right : queue.append(popped.right)
        
        return result