class Solution:
    def delete_node(self, head, x):
        #code here
        temp = head
        
        if x == 1:
            if head.next:
                head.next.prev = None
            return head.next
        
        count=1
        while count < x :
            temp = temp.next
            count+=1
        
        if temp.next:
            temp.next.prev = temp.prev
        if temp.prev:
            temp.prev.next = temp.next
        
        return head
        
       