# Last updated: 11/24/2025, 9:23:14 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None : 
            return []
        queue = []
        queue.append(root)
        result = []

        while len(queue) > 0 :
            n = len(queue)
            temp = []
            while n > 0 : 
                r = queue.pop(0)
                temp.append(r.val)

                if r.left is not None :
                    queue.append(r.left) 
                if r.right is not None :
                    queue.append(r.right) 

                n-=1
            
            result.append(temp)
        
        return result