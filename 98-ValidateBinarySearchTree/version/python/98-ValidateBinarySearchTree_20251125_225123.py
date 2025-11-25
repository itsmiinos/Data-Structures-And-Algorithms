# Last updated: 11/25/2025, 10:51:23 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None : 
            return True
        return self.helper(root , float('-inf') , float('inf'))
    
    def helper(self , root , min , max) -> bool : 
        if root is None : 
            return True
        
        if root.val > min and root.val < max : 
            left = self.helper(root.left , min , root.val)
            right = self.helper(root.right , root.val , max)
            return left and right
        else :
            return False