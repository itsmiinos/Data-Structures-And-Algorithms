# Last updated: 8/13/2025, 8:22:54 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        result = []

        while curr is not None : 
            if curr.left is None : 
                result.append(curr.val)
                curr = curr.right
            
            else : 
                currp1 = curr.left
                while currp1.right is not None and currp1.right!= curr : 
                    currp1 = currp1.right
                
                if currp1.right is None : 
                    currp1.right = curr
                    
                    curr = curr.left
                
                else : 
                    currp1.right = None
                    result.append(curr.val)
                    curr = curr.right
        
        return result