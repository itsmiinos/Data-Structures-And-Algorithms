# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.greater = 0
        self.helper(root)
        return root
    
    def helper(self , root : TreeNode) -> None : 
        if root is None : 
            return
        
        self.helper(root.right)

        self.greater = root.val + self.greater
        root.val = self.greater

        self.helper(root.left)

