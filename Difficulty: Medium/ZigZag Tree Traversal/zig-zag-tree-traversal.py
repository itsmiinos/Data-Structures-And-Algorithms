'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''


class Solution:
    #Function to store the zig zag order traversal of tree in a list.
    def zigZagTraversal(self, root):
        my_queue = []
        result = []
        my_queue.append(root)
        level = 1
        
        if root is None : 
            return []
        
        while len(my_queue) > 0  : 
            n = len(my_queue)
            temp_list = []
            while n > 0 :
                temp_node = my_queue.pop(0)
                temp_list.append(temp_node.data)
                
                if temp_node.left : 
                    my_queue.append(temp_node.left)
                if temp_node.right : 
                    my_queue.append(temp_node.right)
                
                n-=1
            if level % 2 == 0 : 
                temp_list.reverse()
            result.append(temp_list)
            level+=1
        return [item for sublist in result for item in sublist]
                