# Last updated: 2/9/2026, 1:21:26 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
9        self.nodes = []
10        self.inOrderTraversal(root)
11
12        l = 0 
13        r = len(self.nodes)-1
14
15        new_root = self.createBalancedTree( l , r)
16
17        return new_root
18    
19    def createBalancedTree(self , left : int , right : int) -> int :
20        if left > right:
21            return None
22
23        mid = int(left + (right - left) / 2)
24
25        root = TreeNode(self.nodes[mid])
26
27        root.left = self.createBalancedTree(left , mid-1)
28        root.right = self.createBalancedTree(mid + 1 ,right)
29
30        return root
31
32    
33
34    def inOrderTraversal(self , root : TreeNode) -> None :
35        if root is None :
36            return None
37        
38        self.inOrderTraversal(root.left)
39        self.nodes.append(root.val)
40        self.inOrderTraversal(root.right)
41
42        return None