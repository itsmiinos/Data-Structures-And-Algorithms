# Last updated: 11/24/2025, 7:53:54 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None and subRoot is not None : 
            return False
        
        if root is not None and subRoot is None : 
            return False
        same = False
        if root.val == subRoot.val : 
            same = self.isSameTree(root , subRoot)
        
        return same or self.isSubtree(root.left , subRoot) or self.isSubtree(root.right , subRoot)
    
    def isSameTree(self , p : 'TreeNode' , q : 'TreeNode') -> bool :
        if p is None and q is not None : 
            return False
        
        if p is not None and q is None : 
            return False
        
        if p is None and q is None : 
            return True
        
        if p.val == q.val : 
            return self.isSameTree(p.left , q.left) and self.isSameTree(p.right , q.right)

        return False