# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        tree_nodes = []
        result = self.helper(root , tree_nodes)
        return result
    
    def helper(self , root : Optional[TreeNode] , tree_node : [int]) -> [int] :
        if root is None : 
            return []
        
        
        self.helper(root.left , tree_node)
        self.helper(root.right , tree_node)
        tree_node.append(root.val)

        return tree_node