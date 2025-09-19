# Last updated: 9/19/2025, 11:09:34 PM
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
        
        left = self.calculateHeight(root.left)
        right = self.calculateHeight(root.right)

        if abs(left - right) > 1 : 
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    
    def calculateHeight(self , root : Optional[TreeNode]) -> int : 

        if root is None : 
            return 0
        
        left = self.calculateHeight(root.left)
        right = self.calculateHeight(root.right)

        return max(left , right) + 1