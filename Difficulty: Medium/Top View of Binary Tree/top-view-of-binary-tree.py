# Tree Node
# class Node:
#     def __init__(self, val):
#         self.right = None
#         self.data = val
#         self.left = None

class Solution:
    #Function to return a list of nodes visible from the top view 
    #from left to right in Binary Tree.
    def topView(self,root):
        # code here
        queue = []
        queue.append(Pair(root , 0))
        hashmap = {}
        
        while len(queue) > 0 : 
            
            popped = queue.pop(0)
            curr_level = popped.v_level
            curr_node = popped.node
            
            if curr_level not in hashmap : 
                hashmap[curr_level] = curr_node.data
            
            if curr_node.left : queue.append(Pair(curr_node.left , curr_level - 1))
            if curr_node.right : queue.append(Pair(curr_node.right , curr_level + 1))
            
        result = []
        for key in sorted(hashmap.keys()) : 
            result.append(hashmap[key])
            
        return result
    

class Pair : 
    def __init__(self , node , vertical_level : int ) : 
        self.v_level = vertical_level
        self.node = node