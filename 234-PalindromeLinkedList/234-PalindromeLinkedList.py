# Last updated: 8/13/2025, 8:20:53 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        prev = None
        slow_next = None
        while fast is not None and fast.next is not None :
            fast = fast.next.next

            slow_next = slow.next
            slow.next = prev
            prev = slow
            slow = slow_next
        
        first = None
        second = None

        if fast is not None : 
            slow = slow.next
        
        first = prev
        second = slow
        
        
        while first is not None and second is not None : 
            if first.val != second.val : 
                return False
            first = first.next
            second = second.next

        
        if first is None and second is None : 
            return True
        
        return False
        


            
            