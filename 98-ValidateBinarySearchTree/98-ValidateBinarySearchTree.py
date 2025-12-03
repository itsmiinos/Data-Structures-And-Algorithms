# Last updated: 12/3/2025, 2:03:37 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isValidBST(self, root: Optional[TreeNode]) -> bool:
9        if root.left is None and root.right is None : 
10            return True
11        
12        return self.helper(root , float('-inf') , float('inf'))
13    
14    def helper(self , root : 'TreeNode', min : int, max : int) -> bool :
15        if root is None : 
16            return True
17        
18        if min < root.val < max :
19            left = self.helper(root.left , min , root.val)
20            right = self.helper(root.right , root.val , max)
21            return left and right
22        else : 
23            return False