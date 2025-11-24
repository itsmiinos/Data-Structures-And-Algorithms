# Last updated: 11/24/2025, 7:41:13 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None : 
            return 0
        
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left , right) + 1