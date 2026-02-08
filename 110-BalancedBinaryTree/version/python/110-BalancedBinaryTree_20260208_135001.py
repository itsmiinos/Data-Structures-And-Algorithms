# Last updated: 2/8/2026, 1:50:01 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isBalanced(self, root: Optional[TreeNode]) -> bool:
9        if root is None : 
10            return True
11        
12        left = self.calculateHeight(root.left)
13        right = self.calculateHeight(root.right)
14
15        if abs(left - right) > 1 :
16            return False
17        
18        return self.isBalanced(root.left) and self.isBalanced(root.right)
19        
20    
21    def calculateHeight(self , root) -> int : 
22        if root is None : 
23            return 0
24        
25        left = self.calculateHeight(root.left)
26        right = self.calculateHeight(root.right)
27
28        return 1 + max(left , right)