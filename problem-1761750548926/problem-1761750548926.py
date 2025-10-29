# Last updated: 10/29/2025, 8:39:08 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None : 
            return True
        
        left = self.checkHeight(root.left)
        right = self.checkHeight(root.right)

        if abs(left - right) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def checkHeight(self , root) -> int : 
        if root is None : 
            return 0
        
        left = self.checkHeight(root.left)
        right = self.checkHeight(root.right)
        
        return 1 + max(left , right)