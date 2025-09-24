# Last updated: 9/24/2025, 11:46:44 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_map = {}

        for i in range(len(inorder)) : 
            index_map[inorder[i]] = i
        
        root = self.createTree(postorder , 0 , len(postorder)-1 , inorder , 0 , len(inorder)-1 , index_map)
        return root
    
    def createTree(self , postorder : list[int] , postStart : int , postEnd : int , inorder : list[int] , inStart : int , inEnd : int , index_map : dict) -> Optional[TreeNode] : 

        if postStart > postEnd or inStart > inEnd : 
            return None
        
        root = TreeNode(postorder[postEnd])
        inRoot = index_map[postorder[postEnd]]
        numsLeft = inRoot - inStart

        root.left = self.createTree(postorder , postStart , postStart + numsLeft - 1, 
        inorder , inStart , inRoot - 1 ,index_map)

        root.right = self.createTree(postorder , postStart + numsLeft , postEnd - 1 , 
        inorder , inRoot + 1 , inEnd , index_map)

        return root

        
