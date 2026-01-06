# Last updated: 1/6/2026, 8:35:32 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
9        queue = []
10        queue.append(root)
11        max_sum = float('-inf')
12        max_level = -1
13        c = 0
14
15        while len(queue) > 0 :
16            n = len(queue)
17            sum = 0
18            c +=1
19            while n > 0 :
20                res = queue.pop(0)
21                sum += res.val
22                if res.left : 
23                    queue.append(res.left)
24                if res.right :
25                    queue.append(res.right)
26                n-=1
27
28            
29            if sum > max_sum :
30                max_sum = sum
31                max_level = c
32        
33        return max_level