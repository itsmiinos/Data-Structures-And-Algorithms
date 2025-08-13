# Last updated: 8/13/2025, 8:23:34 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        temp = head

        if head is None or head.next is None or k == 0: 
            return head

        length = 0
        while temp is not None : 
            temp = temp.next
            length+=1
        
        k = k % length
        
        if k == 0 : 
            return head
        
        fast = head

        for _ in range(k+1) : 
            fast = fast.next

        slow = head

        while fast is not None :
            slow = slow.next
            fast = fast.next
        
        new_head = slow.next
        slow.next = None

        fast2 = new_head

        while fast2.next is not None : 
            fast2 = fast2.next
        
        fast2.next = head

        return new_head