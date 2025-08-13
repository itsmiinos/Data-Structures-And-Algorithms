# Last updated: 8/13/2025, 8:22:47 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        my_queue = []
        result = []
        if root is None : 
            return []
        my_queue.append(root)

        while len(my_queue) > 0 :
            n = len(my_queue)
            temp_list = []

            while n > 0 : 
                temp_node = my_queue.pop(0)
                temp_list.append(temp_node.val)

                if temp_node.left : 
                    my_queue.append(temp_node.left)
                if temp_node.right :
                    my_queue.append(temp_node.right)
                
                n-=1
            result.append(temp_list)
        return result