'''
class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None

'''

class Solution:
    
    #Function to convert binary tree into circular doubly linked list.
    def bTreeToClist(self, root):
        #Your code here
        if root is None : 
            return None
            
        left = self.bTreeToClist(root.left)
        right = self.bTreeToClist(root.right)
        
        if left is None and right is None : 
            root.left = root
            root.right = root
            return root
        
        elif left is not None and right is None :
            root.left = root
            root.right = root
            return self.combineTwoCDLL(left , root)
            
        elif left is None and right is not None : 
            root.left = root
            root.right = root
            return self.combineTwoCDLL(root , right)
            
        elif left is not None and right is not None :
            root.left = root
            root.right = root
            return self.combineTwoCDLL(self.combineTwoCDLL(left , root) , right)
        
    
    def combineTwoCDLL(self , head1 : Node , head2 : Node) : 
        
        last_node_one = head1.left
        last_node_one.right = head2
        last_node_two = head2.left
        last_node_two.right = head1
        
        head2.left = last_node_one
        head1.left = last_node_two
        
        return head1

        
        