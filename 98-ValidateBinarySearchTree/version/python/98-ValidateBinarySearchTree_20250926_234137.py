# Last updated: 9/26/2025, 11:41:37 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        result = self.helper(root , float('-inf') , float('inf'))
        return result
    
    def helper(self , root : TreeNode , min : int , max : int) -> bool :

        if root is None : 
            return True
        
        if root.val <= min or root.val >= max : 
            return False
        
        left = self.helper(root.left , min , root.val)
        right = self.helper(root.right , root.val, max)

        return left and right