# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None : 
            return None

        left = self.flatten(root.left)
        right = self.flatten(root.right)

        if root.left is None and root.right is None : 
            return root
        
        elif root.left is not None and root.right is None : 
            left_child = root.left
            root.right = left_child
            root.left = None
            return left
        
        elif root.left is None and root.right is not None : 
            return right
        
        elif root.left is not None and root.right is not None : 
            left_child = root.left
            right_child = root.right

            root.right = left_child
            root.left = None

            tail = left
            while tail.right:
                tail = tail.right
            tail.right = right_child

            return root
        
