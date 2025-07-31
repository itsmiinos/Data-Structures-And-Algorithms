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
    
    def helper(self , root : TreeNode , min : int , max : int) -> int :
        if root is None : 
            return True
        
        if min > root.val or root.val > max : 
            return False
        
        left = self.helper(root.left , min , root.val - 1)
        right = self.helper(root.right , root.val + 1 , max)

        return left & right