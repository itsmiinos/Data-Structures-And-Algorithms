# Last updated: 11/26/2025, 10:49:06 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
9        inorder_map = {}
10        for i in range(len(inorder)):
11            inorder_map[inorder[i]] = i
12
13        self.preIndex = 0
14
15        return self.solve(preorder, inorder_map, 0, len(inorder) - 1)
16    
17    def solve(self, preorder, inorder_map, start, end):
18        if start > end:
19            return None
20
21        root_val = preorder[self.preIndex]
22        self.preIndex += 1
23        
24        root = TreeNode(root_val)
25     
26        root_index = inorder_map[root_val]
27               
28        left_count = root_index - start
29
30        root.left = self.solve(preorder, inorder_map, start, root_index - 1)
31        root.right = self.solve(preorder, inorder_map, root_index + 1, end)
32
33        return root