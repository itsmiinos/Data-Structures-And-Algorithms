# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree_nodes = []
        result = self.helper(root , tree_nodes)
        return result
    
    def helper(self , root : Optional[TreeNode] , tree_node : [int]) -> [int] :
        if root is None : 
            return []
        
        tree_node.append(root.val)
        self.helper(root.left , tree_node)
        self.helper(root.right , tree_node)

        return tree_node