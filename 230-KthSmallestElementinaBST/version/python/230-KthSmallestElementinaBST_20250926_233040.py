# Last updated: 9/26/2025, 11:30:40 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        curr = root
        n = 0
        stack = []

        while curr is not None or len(stack) > 0 : 

            while curr is not None : 
                stack.append(curr)
                curr = curr.left
            
            curr = stack.pop(-1)
            n+=1
            if n == k : 
                return curr.val
            curr = curr.right
        

