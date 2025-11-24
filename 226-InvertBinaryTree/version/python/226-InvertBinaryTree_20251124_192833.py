# Last updated: 11/24/2025, 7:28:33 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None : 
            return None
        
        left = root.left
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(left)

        return root