# Last updated: 12/15/2025, 8:45:55 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        self.max_sum = float('-inf')
10        self.solve(root)
11
12        return self.max_sum
13    
14    def solve(self , root : 'TreeNode') -> None : 
15
16        if root is None : 
17            return 0
18
19        left = max(0 , self.solve(root.left))
20        right = max(0 , self.solve(root.right))
21
22        self.max_sum = max(self.max_sum , left + right + root.val)
23
24        return root.val + max(left , right)
25      