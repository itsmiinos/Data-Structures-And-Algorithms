# Last updated: 8/13/2025, 8:20:13 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        self.tree_string = ""
        self.dfs(root)
        return self.tree_string
    
    def dfs(self , root) : 
        if root is None : 
            self.tree_string += "N" + " "
            return
        
        self.tree_string += str(root.val) + " "
        self.dfs(root.left)
        self.dfs(root.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        values = data.split(" ")
        index = [0]
        root = self.helper(index,values)
        return root
    
    def helper(self , index : int , values : list[str]) :
        if values[index[0]] == 'N' :
            index[0] +=1
            return None
        
        node = TreeNode(int(values[index[0]]))
        index[0]+=1
        node.left = self.helper(index , values)
        node.right = self.helper(index , values)

        return node


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))