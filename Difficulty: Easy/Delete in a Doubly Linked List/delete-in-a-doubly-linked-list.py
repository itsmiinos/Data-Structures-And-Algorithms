class Solution:
    def delete_node(self, head, x):
        #code here
        
        if x == 1 : 
            newHead = head.next
            if newHead : 
                newHead.prev = None
                head = newHead
            return head
        
        temp = head
        counter = 1
        
        while temp is not None : 
            if counter == x : 
                if temp.prev : 
                    temp.prev.next = temp.next
                if temp.next : 
                    temp.next.prev = temp.prev
                break
        
            temp = temp.next
            counter +=1
        
        return head