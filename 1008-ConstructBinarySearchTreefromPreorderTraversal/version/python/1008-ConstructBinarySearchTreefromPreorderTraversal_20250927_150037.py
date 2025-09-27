# Last updated: 9/27/2025, 3:00:37 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        
        root = self.helper(preorder , 0 , len(preorder)-1)
        return root
    
    def helper(self , preorder : list[int] , start : int , end : int) -> TreeNode : 

        if start > end : 
            return None
        
        root = TreeNode(preorder[start])
        
        split = start + 1
        while split <= end and preorder[split] < root.val:
            split += 1

        root.left = self.helper(preorder, start + 1, split - 1)
        root.right = self.helper(preorder, split, end)

        return root

