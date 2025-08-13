# Last updated: 8/13/2025, 8:22:48 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None :
            return True
        if p is None and q is not None :
            return False
        if p is not None and q is None :
            return False
        if p.val != q.val : 
            return False 
        
        temp1 = self.isSameTree(p.left , q.left)
        temp2 = self.isSameTree(p.right , q.right)

        return temp1 and temp2