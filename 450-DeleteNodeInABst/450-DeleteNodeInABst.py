# Last updated: 8/13/2025, 8:19:42 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if root is None : 
            return None

        #first find the node : 
        if root.val < key : 
            root.right = self.deleteNode(root.right , key)
            
        
        elif root.val > key : 
            root.left = self.deleteNode(root.left , key)
        #you found the node : 
        else : 
            #now we have three cases : 1. Where the root has only left child , 2. Where the root has only right child , 3. Where the root has left and right child

            if root.left == None and root.right == None : 
                return None

            elif root.left != None and root.right == None : 
                return root.left
            
            elif root.left == None and root.right != None : 
                return root.right
            
            else : 
                left_maximum = self.findMaximum(root.left)
                root.val = left_maximum
                root.left = self.deleteNode(root.left , left_maximum)
                return root
        
        return root
    
    def findMaximum(self , root : TreeNode) : 
        while root.right is not None : 
            root = root.right
        
        return root.val
    