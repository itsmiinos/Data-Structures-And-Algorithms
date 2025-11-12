# Last updated: 11/13/2025, 12:15:35 AM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root is None : 
            return 0
        
        return self.solve(root , root.val)
    
    def solve(self , root , maxValue) -> int : 
        if root is None : return 0
        res = 0
        if root.val >= maxValue :
            res = 1
        
        maxValue = max(maxValue , root.val)
        
        left = self.solve(root.left , maxValue)
        right = self.solve(root.right , maxValue)

        return res + left + right