# Last updated: 12/4/2025, 10:55:31 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        self.maxi = float('-inf')
10        self.helper(root)
11        return self.maxi
12    
13    def helper(self , root) -> int : 
14
15        if root is None : 
16            return 0
17        
18        left = max(0 , self.helper(root.left))
19        right = max(0 , self.helper(root.right))
20
21        self.maxi = max(self.maxi , left + right + root.val)
22
23        return max(left , right) + root.val