# Last updated: 9/21/2025, 10:26:44 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = []

        if root is None : 
            return 0

        queue.append([root , 1])

        max_width = 1

        while len(queue) > 0 : 
            
            n = len(queue)
            left_index = queue[0][1]
            right_index = queue[-1][1]
            max_width = max(max_width , right_index - left_index + 1)

            for i in range (n) : 

                node , index = queue.pop(0)
                

                if node.left is not None : 
                    queue.append([node.left , index * 2])
                    if i == 0 :
                        left_index = index * 2
                if node.right is not None : 
                    queue.append([node.right , (index * 2) + 1])
                    if i == n-1 :
                        right_index = (index * 2) + 1
            
            
            
                
        
        return max_width