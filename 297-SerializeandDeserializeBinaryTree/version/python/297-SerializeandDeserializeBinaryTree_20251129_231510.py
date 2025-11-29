# Last updated: 11/29/2025, 11:15:10 PM
1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Codec:
9
10    def serialize(self, root):
11        """Encodes a tree to a single string.
12        
13        :type root: TreeNode
14        :rtype: str
15        """
16        result = []
17        def dfs(root) : 
18            if root is None : 
19                result.append("N")
20                return
21            result.append(str(root.val))
22            dfs(root.left)
23            dfs(root.right)
24        
25        dfs(root)
26        return ",".join(result)
27
28    def deserialize(self, data):
29        """Decodes your encoded data to tree.
30        
31        :type data: str
32        :rtype: TreeNode
33        """
34        r = data.split(",")
35        self.i = 0
36        def dfs() :
37            if r[self.i] == "N" : 
38                self.i +=1
39                return None
40            
41            root = TreeNode(int(r[self.i]))
42            self.i+=1
43            root.left = dfs()
44            root.right = dfs()
45
46            return root
47        return dfs()
48
49        
50
51# Your Codec object will be instantiated and called as such:
52# ser = Codec()
53# deser = Codec()
54# ans = deser.deserialize(ser.serialize(root))