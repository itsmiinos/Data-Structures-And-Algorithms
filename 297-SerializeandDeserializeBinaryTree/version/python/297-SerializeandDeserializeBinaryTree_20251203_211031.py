# Last updated: 12/3/2025, 9:10:31 PM
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
21            
22            result.append(str(root.val))
23            dfs(root.left)
24            dfs(root.right)
25        
26        dfs(root)
27
28        return ",".join(result)
29
30    def deserialize(self, data):
31        """Decodes your encoded data to tree.
32        
33        :type data: str
34        :rtype: TreeNode
35        """
36        res = data.split(",")
37        self.idx = 0
38        def dfs() :
39            if res[self.idx] == "N" :
40                self.idx +=1
41                return None
42            root = TreeNode(int(res[self.idx]))
43            self.idx +=1
44            root.left = dfs()
45            root.right = dfs()
46
47            return root
48        
49        return dfs()
50        
51
52# Your Codec object will be instantiated and called as such:
53# ser = Codec()
54# deser = Codec()
55# ans = deser.deserialize(ser.serialize(root))