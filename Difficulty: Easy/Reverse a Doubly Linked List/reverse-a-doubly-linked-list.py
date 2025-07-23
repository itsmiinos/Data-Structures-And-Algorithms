'''
class DLLNode:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
'''

class Solution:
    def reverseDLL(self, head):
        #return head of reverse doubly linked list
        curr = head
        prev = None
        
        while curr is not None : 
            curr_next = curr.next
            curr.next = prev
            curr.prev = curr_next
            prev = curr
            curr = curr_next
            
            
        
        return prev