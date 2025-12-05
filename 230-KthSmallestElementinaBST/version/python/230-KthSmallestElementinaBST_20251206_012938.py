# Last updated: 12/6/2025, 1:29:38 AM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        stack = []
10        curr = root
11        n = 0
12
13        while curr is not None or stack is not None : 
14
15            while curr is not None : 
16                stack.append(curr)
17                curr = curr.left
18            
19            curr = stack.pop(-1)
20            n+=1
21
22            if n == k : 
23                return curr.val
24            
25            curr = curr.right
26        
27        return -1
28