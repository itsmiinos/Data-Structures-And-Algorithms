# Last updated: 11/26/2025, 9:31:33 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
9        curr = root
10        n = 0
11        stack = []
12
13        while curr is not None or stack is not None : 
14            while curr is not None : 
15                stack.append(curr)
16                curr = curr.left
17
18            curr = stack.pop(-1)
19            n+=1
20
21            if n == k : 
22                return curr.val
23            
24            curr = curr.right
25        
26        return -1