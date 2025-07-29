# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        hashmap = {}

        for i in range(len(inorder)) : 
            hashmap[inorder[i]] = i
        
        result = self.helper(preorder , 0 , len(preorder)-1 , inorder , 0 , len(inorder)-1 , hashmap)
        return result
    
    def helper(self , preorder : list[int] , ps , pe , inorder : list[int] , inos , inoe , hashmap) -> int : 

        if (ps > pe) or (inos > inoe) : 
            return None

        root_value = preorder[ps]
        root_index = hashmap[root_value]
        left_count = root_index - inos
        
        root = TreeNode(root_value)

        root.left = self.helper(preorder , ps + 1 , ps + left_count , inorder , inos , root_index - 1 , hashmap)
        root.right = self.helper(preorder , ps + left_count + 1 , pe , inorder , root_index+1 , inoe , hashmap)

        return root