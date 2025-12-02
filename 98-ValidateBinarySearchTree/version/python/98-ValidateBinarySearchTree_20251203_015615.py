# Last updated: 12/3/2025, 1:56:15 AM
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
11        return self.helper(root , float('-inf') , float('inf'))
12    
13    def helper(self , root , min , max) -> bool : 
14        if root is None : 
15            return True
16        
17        if root.val > min and root.val < max : 
18            left = self.helper(root.left , min , root.val)
19            right = self.helper(root.right , root.val , max)
20            return left and right
21        else :
22            return False