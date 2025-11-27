# Last updated: 11/27/2025, 9:57:37 PM
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
17
18        def dfs(root) :
19            if root is None : 
20                result.append("N")
21                return
22            
23            result.append(str(root.val))
24            dfs(root.left)
25            dfs(root.right)
26        
27        dfs(root)
28        return ",".join(result)
29        
30
31    def deserialize(self, data):
32        """Decodes your encoded data to tree.
33        
34        :type data: str
35        :rtype: TreeNode
36        """
37        res = data.split(",")
38        self.i = 0
39
40        def dfs() : 
41            if res[self.i] == "N" : 
42                self.i+=1
43                return None
44            
45            root = TreeNode(int(res[self.i]))
46            self.i+=1
47            root.left = dfs()
48            root.right = dfs()
49
50            return root
51        
52        return dfs()
53        
54
55# Your Codec object will be instantiated and called as such:
56# ser = Codec()
57# deser = Codec()
58# ans = deser.deserialize(ser.serialize(root))