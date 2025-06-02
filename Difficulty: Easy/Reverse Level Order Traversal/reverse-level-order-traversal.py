'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    def reverseLevelOrder(self,root):
        # code here
        my_queue = []
        result = []
        my_queue.append(root)
        
        while len(my_queue) > 0 :
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
            
            result.append(temp_list)
        self.reverseResult(result)
        return [element for sublist in result for element in sublist]
    
    def reverseResult(self , my_array) :
        left = 0
        right = len(my_array)-1
        
        while left <=right : 
            [my_array[left] , my_array[right]] = [my_array[right] , my_array[left]]
            
            left+=1
            right-=1
        
        
        
        
        
        
        
        
        
        