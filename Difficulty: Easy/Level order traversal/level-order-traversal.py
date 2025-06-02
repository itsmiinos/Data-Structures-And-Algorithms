"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
class Solution:
    def levelOrder(self, root):
        # Your code here
        my_queue = []
        my_queue.append(root)
        result = []
        while (len(my_queue) > 0 ) :
            n = len(my_queue)
            temp_list = []
            while (n > 0) : 
                temp = my_queue.pop(0)
                temp_list.append(temp.data)
                if temp.left:
                    my_queue.append(temp.left)
                if temp.right:
                    my_queue.append(temp.right)
                n-=1
            result.append(temp_list)
        return result