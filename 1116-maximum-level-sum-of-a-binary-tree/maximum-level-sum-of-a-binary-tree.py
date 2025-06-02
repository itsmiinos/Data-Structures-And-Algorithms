# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import sys
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        my_queue = []
        result = 0
        my_queue.append(root)
        level = 1
        maxSum = -sys.maxsize
        while len(my_queue) > 0 :
            n = len(my_queue)
            sum = 0
            while n > 0 :
                temp_node = my_queue.pop(0)
                sum = sum + temp_node.val
                
                if temp_node.left : 
                    my_queue.append(temp_node.left)
                if temp_node.right : 
                    my_queue.append(temp_node.right)
                
                n-=1
            if maxSum < sum : 
                maxSum = sum
                max_sum_level = level
            level +=1
        return max_sum_level