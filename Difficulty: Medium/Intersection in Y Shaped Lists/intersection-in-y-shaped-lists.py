'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''
class Solution:
    def intersectPoint(self, head1, head2):
        # code here
        if head1 is None and head2 is None : 
            return
        
        temp1 = head1
        temp2 = head2
        
        while temp1!=temp2 :
            temp1 = temp1.next
            temp2 = temp2.next
            
            if temp1 is None : temp1 = head2
            if temp2 is None : temp2 = head1
        
        return temp1