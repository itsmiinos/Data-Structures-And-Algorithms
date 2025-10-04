# Last updated: 10/5/2025, 1:11:25 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast is not None and n > 0 : 
            fast = fast.next
            n-=1
        
        if fast is None : 
            return head.next
        
        while fast.next is not None :
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next

        return head
