
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def sortedMerge(self,head1, head2):
        # code here
        if head1 is None and head2 is None : 
            return None
        elif head1 is None and head2 is not None :
            return head2
        elif head1 is not None and head2 is None : 
            return head1
        
        dummyNode = Node(-1)
        temp = dummyNode
        
        temp1 = head1
        temp2 = head2
        
        while temp1 is not None and temp2 is not None : 
            if temp1.data < temp2.data :
                temp.next = temp1
                temp1 = temp1.next
            else :
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        
        if temp1 :
            temp.next = temp1
        else :
            temp.next = temp2
        
        return dummyNode.next